import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Log token status (for debugging only - usionyeshe token halisi)
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN haijapatikana. Hakikisha iko kwenye faili la .env")

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Karibu Zephyr Products Assistant!\n\n"
        "Andika /help kuona orodha ya bidhaa au kupata msaada 😊"
    )

# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 Bidhaa tunazouza:\n"
        "🧴 Cosmetics\n"
        "🦷 Dawa za meno\n"
        "🍯 Bee pollen\n"
        "📱 Simu\n"
        "💻 Computers\n"
        "🏠 Malabo ya ndani\n"
        "👕 Nguo za kiume na za kike\n"
        "👟 Viatu aina zote\n\n"
        "Lipa kupitia M-Pesa: 0740233767 📲"
    )

# Main function
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    
    # Start bot
    app.run_polling()
