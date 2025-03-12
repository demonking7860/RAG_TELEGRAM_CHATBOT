import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load articles
with open("battery_articles.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

# Convert articles into embeddings
titles, texts = [], []
for article in articles:
    titles.append(article["title"])
    texts.append(article["content"])

embeddings = model.encode(texts, convert_to_numpy=True)

# Store embeddings in FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Save FAISS index & metadata
faiss.write_index(index, "faiss_index.bin")
with open("titles.json", "w", encoding="utf-8") as f:
    json.dump(titles, f)

print(f"✅ FAISS embeddings stored for {len(titles)} articles!")
