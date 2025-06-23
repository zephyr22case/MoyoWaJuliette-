import os
from dotenv import load_dotenv
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Karibu message
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    text = f"Karibu {user} kwenye Zephyr Products 🛍️\nChagua huduma:"
    buttons = [
        [KeyboardButton("/picha"), KeyboardButton("/bei")],
        [KeyboardButton("/bonus"), KeyboardButton("/hali")],
        [KeyboardButton("/inbox")]
    ]
    reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text(text, reply_markup=reply_markup)

# Command: picha
async def picha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🖼️ Hizi hapa baadhi ya bidhaa zetu:")
    # mfano wa picha moja – ongeza zingine kama unavyopenda
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="https://example.com/path/to/product.jpg",
        caption="🌿 Sabuni ya Asili - TSh 5,000"
    )

# Command: bei
async def bei(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💰 Bei za bidhaa zetu:\n"
        "- Sabuni ya Asili: TSh 5,000\n"
        "- Dawa ya meno ya Asili: TSh 6,000\n"
        "- Bee Pollen 100g: TSh 12,000\n"
        "- Viatu vya Kisasa: TSh 35,000+\n"
        "- Simu na Computer: Tafadhali tuandikie kupitia /inbox\n"
    )
    await update.message.reply_text(text)

# Command: bonus
async def bonus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎁 Bonus ya wiki hii: Nunua bidhaa 3 upate moja bure! 🛍️")

# Command: hali
async def hali(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📦 Tafadhali tuma namba yako ya oda kupitia /inbox ili tuangalie hali ya manunuzi yako.")

# Command: inbox
async def inbox(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📥 Tuma ujumbe wako moja kwa moja hapa na timu yetu itakujibu ndani ya muda mfupi.")

# Main App
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("picha", picha))
    app.add_handler(CommandHandler("bei", bei))
    app.add_handler(CommandHandler("bonus", bonus))
    app.add_handler(CommandHandler("hali", hali))
    app.add_handler(CommandHandler("inbox", inbox))

    print("✅ Bot iko hewani...")
    app.run_polling()

if __name__ == "__main__":
    main()
