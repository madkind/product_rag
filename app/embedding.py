from transformers import LongformerTokenizer, LongformerModel
import torch

class XenonLampEmbeddingSystem:
    def __init__(self, model_name="allenai/longformer-base-4096"):
        self.tokenizer = LongformerTokenizer.from_pretrained(model_name)
        self.model = LongformerModel.from_pretrained(model_name)
        self.embedding_dim = self.model.config.hidden_size

    def generate_embedding(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", max_length=4096, truncation=True)
        # Set global attention on [CLS] token
        inputs['global_attention_mask'] = torch.zeros_like(inputs['attention_mask'])
        inputs['global_attention_mask'][:, 0] = 1
        with torch.no_grad():
            outputs = self.model(**inputs)
            last_hidden_state = outputs.last_hidden_state  # (batch_size, seq_len, hidden_size)
        # Use the embedding of the [CLS] token (the first token)
        embedding = last_hidden_state[:, 0].squeeze().numpy()  # (hidden_size,)
        return embedding

if __name__ == "__main__":
    embedding_system = XenonLampEmbeddingSystem()
    emb = embedding_system.generate_embedding("Example content")
    print(emb)