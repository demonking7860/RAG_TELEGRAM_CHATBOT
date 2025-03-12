import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# ✅ Load preprocessed articles
with open("battery_articles.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

# ✅ Load Sentence Transformer Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# ✅ Convert articles into embeddings
titles = [article["title"] for article in articles]
texts = [article["content"] for article in articles]
embeddings = model.encode(texts, convert_to_numpy=True)

# ✅ Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)  # L2 Distance-based index
index.add(embeddings)  # Add vectors to index

# ✅ Save the index
faiss.write_index(index, "faiss_index.bin")

# ✅ Save titles separately for retrieval
with open("titles.json", "w", encoding="utf-8") as f:
    json.dump(titles, f)

print("✅ FAISS index created and saved as 'faiss_index.bin'")
