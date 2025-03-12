import os
import requests
from search import retrieve_relevant_data

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def fallback_to_llm(user_query):
    """Uses LLM (Groq LLaMA 3 or DeepSeek R1) if RAG fails."""
    prompt = f"""
    You are a battery expert chatbot. Answer the following question correctly.

    User's Question: {user_query}

    If the question is unrelated to batteries, provide a polite, general response.
    """

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}", "Content-Type": "application/json"}
    
    data = {
        "model": "llama3-8b-8192",  # ✅ Use Groq LLaMA 3 or DeepSeek R1
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.5,
        "max_tokens": 500
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return "⚠️ Sorry, I couldn't find an answer to your question. Please rephrase or ask a different query."

def generate_answer(user_query):
    """First attempts RAG-based retrieval, then falls back to LLM, and finally to a default message."""
    best_results = retrieve_relevant_data(user_query)

    # ✅ If RAG retrieval is successful, return structured answer
    if best_results:
        context_text = "\n\n".join([f"📌 **{res['title']}**:\n{res['content'][:800]}" for res in best_results])
        return f"📖 **Based on our knowledge base:**\n{context_text}"

    # ❌ If RAG fails, use LLM fallback
    llm_response = fallback_to_llm(user_query)

    # ❌ If LLM also fails, return predefined response
    if "I don't know" in llm_response or len(llm_response) < 10:
        return "⚠️ I'm not sure about that. Try rephrasing your question or visiting [Battery University](https://batteryuniversity.com)."
    
    return llm_response
