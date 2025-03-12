import json
import faiss
import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

# ✅ Load FAISS index and article data
index = faiss.read_index("faiss_index.bin")
with open("titles.json", "r", encoding="utf-8") as f:
    titles = json.load(f)
with open("battery_articles.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

# ✅ Load Sentence Transformer Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Prepare BM25 for keyword-based retrieval
corpus = [article["content"] for article in articles]
tokenized_corpus = [doc.lower().split() for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus)

def retrieve_relevant_data(query, top_k=3):
    """Hybrid Search: FAISS (semantic) + BM25 (keyword-based)"""
    query_embedding = model.encode([query], convert_to_numpy=True)

    # ✅ FAISS Search
    _, indices = index.search(query_embedding, top_k)
    faiss_results = [articles[idx] for idx in indices[0] if 0 <= idx < len(articles)]

    # ✅ BM25 Search
    bm25_scores = bm25.get_scores(query.lower().split())
    top_bm25_indices = np.argsort(bm25_scores)[::-1][:top_k]
    bm25_results = [articles[idx] for idx in top_bm25_indices]

    # ✅ Merge FAISS + BM25 results
    combined_results = {res["title"]: res["content"] for res in (faiss_results + bm25_results)}
    
    return [{"title": k, "content": v} for k, v in combined_results.items() if v]
