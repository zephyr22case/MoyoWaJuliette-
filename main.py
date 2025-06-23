import logging
import os
from dotenv import load_dotenv
from telegram import Update, InputMediaPhoto
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Token haijapatikana. Tafadhali weka token kwenye .env")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Dummy data kwa bidhaa na picha
PRODUCT_IMAGES = {
    "simu": "https://example.com/simu.jpg",
    "computer": "https://example.com/computer.jpg",
    "malabo": "https://example.com/malabo.jpg",
    "nguo_kiume": "https://example.com/nguo_kiume.jpg",
    "nguo_kike": "https://example.com/nguo_kike.jpg",
    "viatu": "https://example.com/viatu.jpg",
    "cosmetics": "https://example.com/cosmetics.jpg",
    "dawa_za_meno": "https://example.com/dawa_za_meno.jpg",
    "bee_pollen": "https://example.com/bee_pollen.jpg",
}

# Hali ya manunuzi dummy
PURCHASE_STATUS = {
    "1234": "Inasafirishwa 🚚",
    "5678": "Imefika katika kituo cha usafirishaji 📦",
    "9999": "Imekamilika na kuwasilishwa ✅",
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Karibu Zephyr Products Assistant!\nTuma /help kuona amri zote."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Amri za Zephyr Products Bot:\n"
        "/start - Karibu\n"
        "/help - Orodha ya amri\n"
        "/bidhaa - Orodha ya bidhaa\n"
        "/picha <jina> - Onyesha picha ya bidhaa\n"
        "/malipo - Maelezo ya malipo\n"
        "/mawasiliano - Jinsi ya kuwasiliana\n"
        "/hali <namba_ya_oda> - Angalia hali ya manunuzi\n"
        "/inbox - Tuma ujumbe kwa huduma kwa wateja\n"
    )

async def bidhaa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bidhaa_za_kuuzwa = (
        "📦 Bidhaa tunazouza:\n"
        "- simu\n"
        "- computer\n"
        "- malabo\n"
        "- nguo_kiume\n"
        "- nguo_kike\n"
        "- viatu\n"
        "- cosmetics\n"
        "- dawa_za_meno\n"
        "- bee_pollen\n"
        "Tumia /picha <jina> kuona picha ya bidhaa"
    )
    await update.message.reply_text(bidhaa_za_kuuzwa)

async def picha(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Tafadhali tuma jina la bidhaa kwa mfano: /picha simu")
        return
    product_key = context.args[0].lower()
    url = PRODUCT_IMAGES.get(product_key)
    if url:
        await update.message.reply_photo(photo=url, caption=f"Picha ya {product_key.replace('_', ' ').title()}")
    else:
        await update.message.reply_text("Samahani, bidhaa hiyo haipo kwenye orodha yetu.")

async def malipo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💰 Malipo hufanyika kupitia M-Pesa namba: 0740233767\n"
        "Tunasafirisha bidhaa nchi nzima Tanzania 🇹🇿"
    )

async def mawasiliano(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Mawasiliano:\n"
        "M-Pesa: 0740233767\n"
        "Telegram: @ZephyrProductsBot\n"
        "WhatsApp: 0740233767\n"
        "Email: info@zephyrproducts.tz"
    )

async def hali(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("Tafadhali tuma namba ya oda, mfano: /hali 1234")
        return
    order_num = context.args[0]
    status = PURCHASE_STATUS.get(order_num)
    if status:
        await update.message.reply_text(f"Hali ya oda yako ({order_num}): {status}")
    else:
        await update.message.reply_text("Samahani, hatujapata taarifa za oda hiyo.")

# Inbox handler - anza kwa simple echo kama mfano
async def inbox(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Tafadhali tuma ujumbe wako. Tutajibu haraka kadri tuwezavyo."
    )

# Catch user text messages to inbox
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text
    # Hapa unaweza kuongeza code kuhifadhi message kwenye DB au kutuma email
    print(f"Ujumbe kutoka kwa {user.first_name} ({user.id}): {text}")
    await update.message.reply_text("Asante kwa ujumbe wako, tutakujibu hivi karibuni.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("bidhaa", bidhaa))
    app.add_handler(CommandHandler("picha", picha))
    app.add_handler(CommandHandler("malipo", malipo))
    app.add_handler(CommandHandler("mawasiliano", mawasiliano))
    app.add_handler(CommandHandler("hali", hali))
    app.add_handler(CommandHandler("inbox", inbox))

    # Handler ya ujumbe wa kawaida
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Zephyr Products Bot iko online...")
    app.run_polling()
