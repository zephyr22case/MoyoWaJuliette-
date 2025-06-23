import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Bot token kutoka BotFather
TOKEN = os.environ.get("BOT_TOKEN")  # Hakikisha umeweka token kama secret kwenye Render

# Orodha ya bidhaa
PRODUCTS = {
    "Simu Aina Zote": "Tunauza simu za aina mbalimbali kama Samsung, iPhone, Tecno, Infinix n.k.",
    "Computer": "Laptop na desktop za kisasa zenye ubora wa hali ya juu.",
    "Malabo ya Ndani": "Mapazia, mablanketi, mikeka, mito n.k.",
    "Nguo za Kiume": "Mashati, suruali, suti, t-shirt na jeans.",
    "Nguo za Kike": "Gauni, sketi, blauzi, top, na mitindo ya kisasa.",
    "Viatu Aina Zote": "Viatu vya michezo, rasmi, ndala na vya kawaida."
}

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[item] for item in PRODUCTS.keys()]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Karibu Zephyr Products! 🛍️\nChagua bidhaa unayotaka kujua zaidi:",
        reply_markup=reply_markup
    )

# Handler wa bidhaa
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in PRODUCTS:
        await update.message.reply_text(PRODUCTS[text])
    else:
        await update.message.reply_text("Samahani, tafadhali chagua bidhaa kutoka kwenye menyu. 🙏")

# Endapo bot inahitaji PORT kwa hosting, Render atahitaji uishughulikie
port = os.environ.get('PORT')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Zephyr Products Bot is running... ✅")
    app.run_polling()
