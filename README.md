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
4. What is the smallest unit I can order?
5. Which luminaire has the SCIP number dd2ddf15-037b-4473-8156-97498e721fb3?

Make sure these queries can definitely be answered correctly.