import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Karibu Zephyr Products Assistant! 😊\n\nAndika jina la bidhaa unayotafuta..."
    )

# Help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Unaweza kuuliza kuhusu:\n- Simu\n- Kompyuta\n- Malabo ya ndani\n- Nguo\n- Viatu\n\nTuma tu jina la bidhaa!"
    )

# Generic message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Sample product replies (unaweza kupanua)
    if "simu" in text:
        reply = "Tunauza simu aina zote! Samsung, iPhone, Tecno, Infinix, n.k.\nWasiliana: 0740 233 767"
    elif "kompyuta" in text or "laptop" in text:
        reply = "Tunatoa laptops zenye ubora – Dell, HP, Lenovo n.k.\nDM kwa bei!"
    elif "viatu" in text:
        reply = "Tunazo viatu vya wanaume na wanawake. Tuma size yako na style upendayo 😊"
    elif "nguo" in text:
        reply = "Nguo mpya zimewasili! Zipo za kiume na za kike. Uliza sasa!"
    else:
        reply = "Samahani, tafadhali eleza zaidi kuhusu bidhaa unayotafuta 🛍️"

    await update.message.reply_text(reply)

# Main function to run the bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Zephyr Products Bot is running...")
    app.run_polling()
