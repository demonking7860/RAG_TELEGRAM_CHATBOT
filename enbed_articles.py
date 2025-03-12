import os
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load articles
DATA_FILE = "battery_articles.json"

with open(DATA_FILE, "r", encoding="utf-8") as f:
    articles = json.load(f)

# Generate embeddings
embeddings = {}
for article in articles:
    title = article["title"]
    content = article["content"]
    embeddings[title] = model.encode(content)

# Save embeddings
np.save("article_embeddings.npy", embeddings)
