import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")
items = ["Mouse", "Headphones", "Keyboard", "Monitor", "Laptop Stand"]
embs = model.encode(items)
index = faiss.IndexFlatL2(embs.shape[1])
index.add(np.array(embs))

def recommend_for_user(user_id: int):
    query = "computer accessories"
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k=3)
    return [items[i] for i in I[0]]
