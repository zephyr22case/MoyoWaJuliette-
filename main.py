import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Weka token yako halali hapa
BOT_TOKEN = "8083188846:AAH7EysBhg_TroN3NEq0rWid0ZOA8GJ8QRk"

# Washa logging kwa debugging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Auto message ya mwanzo kwa /start
WELCOME_MESSAGE = (
    "🎉 *Karibu ZephyrProducts!* 🌬️\n"
    "👋🏽 Tupo hapa kukuletea bidhaa *bora, za asili, salama,* na kwa bei unayoimudu!\n"
    "Kutoka kwenye *simu za kisasa*, 💻 *kompyuta*, 🧴 *cosmetics*, hadi 👚 *nguo na viatu vya aina zote* — tunajali mahitaji yako.\n\n"
    "✨ *Jisikie huru kubonyeza menyu ili kuchagua bidhaa, kuuliza bei, au kuwasiliana nasi moja kwa moja.*\n"
    "📦 Usafirishaji unapatikana *nchi nzima 🇹🇿* — salama, haraka, na kwa heshima.\n\n"
    "💌 *ZephyrProducts — upepo wa bidhaa bora!*"
)

# Handler ya /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("🛍️ Orodha ya Bidhaa"), KeyboardButton("💰 Bei za Bidhaa")],
        [KeyboardButton("🎁 Bonus"), KeyboardButton("📦 Hali ya Manunuzi")],
        [KeyboardButton("🖼️ Picha za Bidhaa"), KeyboardButton("📬 Inbox")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(WELCOME_MESSAGE, reply_markup=reply_markup, parse_mode='Markdown')

# Command zingine za mfano
async def bonus(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎁 Leo ukinunua bidhaa 3 au zaidi, utapata *FREE DELIVERY*! 🚚")

async def bidhaa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = (
        "🛒 *Bidhaa Zilizopo:*\n"
        "- Simu za kisasa (Samsung, iPhone, Tecno...)\n"
        "- Kompyuta na Laptop\n"
        "- Dawa za meno, cosmetics\n"
        "- Nguo za kike na kiume\n"
        "- Viatu vya aina zote\n"
        "- Malabo ya ndani\n\n"
        "Tumia menu au andika jina la bidhaa kupata bei na maelezo."
    )
    await update.message.reply_text(msg, parse_mode='Markdown')

async def inbox(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📬 Tafadhali andika ujumbe wako hapa. Tutakujibu haraka iwezekanavyo.")

# Main bot
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bonus", bonus))
    app.add_handler(CommandHandler("bidhaa", bidhaa))
    app.add_handler(CommandHandler("inbox", inbox))
    
    print("🤖 Bot inafanya kazi...")
    app.run_polling()

if __name__ == "__main__":
    main()
