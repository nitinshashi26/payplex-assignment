from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
knowledge_base = [
    ("return policy", "Customers can return products within 30 days."),
    ("shipping time", "Standard shipping takes 3–5 days."),
]
vectors = np.array([model.encode(k[0]) for k in knowledge_base])

def retrieve_context(query: str):
    q_vec = model.encode(query)
    scores = vectors @ q_vec
    idx = int(np.argmax(scores))
    return knowledge_base[idx][1]
