import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from generate_answer import generate_answer

# ✅ Load Telegram API Key
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# ✅ Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Predefined general responses
GENERAL_RESPONSES = {
    "hi": "Hello! How can I assist you today? 😊",
    "hello": "Hey there! Ask me anything about batteries 🔋",
    "how are you": "I'm just a bot, but I'm always ready to help!",
    "who are you": "I'm VoltQ AI, here to answer your battery-related questions!",
    "what can you do": "I can provide information about batteries, answer queries, and assist with general knowledge!"
}

async def start(update: Update, context):
    """Sends a greeting message."""
    await update.message.reply_text("Hello! 🔋 Ask me anything about batteries, and I'll try my best to help.")

async def handle_query(update: Update, context):
    """Handles user queries using RAG first, then falls back to LLM."""
    user_message = update.message.text.lower()

    # ✅ Check predefined general responses
    if user_message in GENERAL_RESPONSES:
        await update.message.reply_text(GENERAL_RESPONSES[user_message])
        return

    await update.message.reply_text("🔍 Searching knowledge base...")
    
    response = generate_answer(user_message)

    # ✅ Split long responses into chunks (Telegram limit: 4096 chars)
    chunk_size = 4000  
    for i in range(0, len(response), chunk_size):
        await update.message.reply_text(response[i:i+chunk_size])

def main():
    """Starts the Telegram bot."""
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("⚠️ TELEGRAM_BOT_TOKEN is missing! Set it as an environment variable.")

    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_query))

    logger.info("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
