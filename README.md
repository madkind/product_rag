Task description:
```
Goal:
Develop a search solution based on PDF documents using a Language Model (LLM).

Part 1: RAG (Retrieval Augmented Generation) with PDF Documents

1. Provided PDF Documents
   You will be given PDF documents with defined content.

2. Search Tool Development
   Create a piece of software in which user queries can be entered. It's sufficient to do this directly in the code; no UI or additional interface is required. Also, there's no need for an interface to upload or select PDFs; you can simply access them via the file system in a fixed location.

3. Retrieval
   Identify relevant sections in the PDF documents based on user queries. Holding this data only in memory is sufficient — persistence is not strictly necessary.

4. Answer Generation
   Generate and present answers using the search results and the LLM. A simple output to stdout (or similar) is fine.

Part 2: Quality Assurance

To validate your approach, here are a few questions we will very likely ask your system during the interview process:

1. How much does the XBO 4000 W/HS XL OFR weigh?
2. Which luminaire is best suited for my home theater?
3. Give me all lamps with at least 1500W and a lifetime of more than 3000 hours.
4. What is the smallest unit I can order? - SKIPPED for now
5. Which luminaire has the SCIP number dd2ddf15-037b-4473-8156-97498e721fb3?

Make sure these queries can definitely be answered correctly.
```


I have put the pdfs to 'data/pdf'. There are 21 of them. All of them are very similiar, they describe Xenon lamps, the language of them is German.

Reading the questions, it seems like naive rag (doc retrival with text similiarty) won't cut when we have hundreds of products. Many questions would need information from all documents - which I wont be fitting into the context in an elegant way for sure. I decide to create an sql database, which I intend compose and run queries against.
I prefer using gemini pro for more complex tasks (generating code ), and flash for the chain to keep costs lower.

Create DB

You can follow along the process @ [create_db.ipynb](create_db.ipynb)
Remarks: 
- I used gemini pro to create the schema based on a subset of the documents
- based on the schema I asked it to create the db schema creation script
   - Feature engineering would have been useful, but I have time constraints.
- based on the schema I asked to create a json representation of extracted data for each document
- based on all of these I asked the llm to create a python script to populate the db based on the jsons




Query Chain

I have implemented the query chaing @ [query.ipynb](query.ipynb)

For starters, I have experimented with create_sql_query_chain. I ended up modifying the default prompt template to give hints about text array fields. I did not want to normalize the schema to keep the setup simple. I picked postgres over SQLlite for array field support.

I have noticed that thinking models perform better, however way slower and costly - so I implemented a separate "thinking" step called "expert advice". 

```
chain = (
    # ask llm to gather information to compose the query
    RunnableLambda(lambda x: {**x, **get_expert_advice(x)})
    # create the query
    | RunnableLambda(lambda x: {**x, "sql": create_sql_query_chain(llm, db, POSTGRES_PROMPT).invoke(x)})
    # run query
    | RunnableLambda(run_sql_query)
    # compose answer
    | RunnableLambda(compose_answer)
)
```

You can see the result report with intermediate results here: [RESULTS](RESULTS.MD)

I would be really happy to talk about the prompt engineering part of the task, however right now I do not have more time to describe it in writing :)