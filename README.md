# RAG Telegram Chatbot

## 📌 Overview
This is a **Retrieval-Augmented Generation (RAG) Telegram Chatbot** that extracts information from battery-related articles and provides intelligent responses using LLMs. It utilizes **FAISS for vector search**, **BM25 for keyword matching**, and **Groq LLaMA 3 API** as a fallback model.

## 🚀 Features
- **Retrieves answers from battery-related articles using RAG**
- **Uses FAISS & BM25 for hybrid search**
- **Integrates with Telegram Bot API for real-time responses**
- **Falls back to Groq LLaMA 3 if no relevant data is found**

---

## 🛠️ Tech Stack
- **Python**
- **Telegram Bot API**
- **FAISS for vector search**
- **BM25 for keyword-based retrieval**
- **Groq LLaMA 3 API for fallback answers**
- **Sentence-Transformers (all-MiniLM-L6-v2)**

---

## 🔧 Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/demonking7860/RAG_TELEGRAM_CHATBOT.git
cd RAG_TELEGRAM_CHATBOT
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**
Create a `.env` file and add:
```
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
```

### **4️⃣ Build FAISS Index**
```bash
python create_faiss_index.py
```

### **5️⃣ Run the Bot**
```bash
python bot.py
```

---

## 📌 Usage
- Start the bot by messaging it on Telegram.
- Ask questions related to **battery technologies**.
- The bot retrieves information using **FAISS + BM25**.
- If no relevant answer is found, it uses **Groq LLaMA 3** for response generation.

---

## 📦 Deployment
### **Deploy on a Server (Render/Heroku/VPS)**
1. Use **Docker** or a cloud platform to deploy the bot.
2. Run it using a background process (`nohup` or `screen`).

### **Deploy using Docker**
```bash
docker build -t rag_telegram_chatbot .
docker run -d -p 5000:5000 --env-file .env rag_telegram_chatbot
```

---

## 🤝 Contributing
Feel free to fork the repo and create pull requests for improvements!

---

## 📜 License
MIT License

---

## 📞 Contact
For any issues, reach out via GitHub or Telegram!
