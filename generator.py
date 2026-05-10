from transformers import pipeline
gen = pipeline("text-generation", model="distilgpt2")

def get_llm_response(query: str, context: str, history: list):
    prompt = f"Context: {context}\nUser: {query}\nBot:"
    output = gen(prompt, max_length=80)[0]["generated_text"]
    return output.replace(prompt, "").strip()
