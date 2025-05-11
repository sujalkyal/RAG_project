# File: services/embedding_utils.py
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_top_k_chunks(question, documents, k=5):
    query_embedding = model.encode(question, convert_to_tensor=True)
    doc_texts = [doc['content'] for doc in documents]
    doc_embeddings = model.encode(doc_texts, convert_to_tensor=True)
    scores = util.pytorch_cos_sim(query_embedding, doc_embeddings)[0]
    top_indices = scores.argsort(descending=True)[:k]
    return [doc_texts[i] for i in top_indices]
