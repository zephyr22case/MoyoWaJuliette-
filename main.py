import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Sanidi logger
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Weka token yako halisi hapa
BOT_TOKEN ="8083188846:AAH7EysBhg_TroN3NEq0rWid0ZOA8GJ8QRk"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Karibu ZephyrProducts Assistant! 😊\n\n"
        "Tumia /bidhaa kuona orodha ya bidhaa au tuma swali lako kuhusu bidhaa yoyote."
    )

# /bidhaa
async def bidhaa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛍️ Hizi ndizo bidhaa tunazouza kwa sasa:\n"
        "- /simu 📱\n"
        "- /computer 💻\n"
        "- /nguo 👚👕\n"
        "- /viatu 👟\n"
        "- /malabo 🛋️\n"
        "\nTumia command ya bidhaa kupata maelezo zaidi!"
    )

# /simu
async def simu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Simu tulizonazo:\n"
        "- Infinix Hot 40: Tsh 450,000\n"
        "- Samsung A14: Tsh 600,000\n"
        "- iPhone 11: Tsh 1,400,000\n"
        "✅ Warranty mwaka 1, zenye chaja & earphones."
    )

# /computer
async def computer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💻 Computer tulizonazo:\n"
        "- Dell Latitude 7490: Tsh 650,000\n"
        "- HP EliteBook 840 G6: Tsh 720,000\n"
        "- MacBook Pro 2017: Tsh 1,450,000\n"
        "💡 Zina processor za kisasa, SSD, na charger original."
    )

# /nguo
async def nguo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👗 Nguo za Kike na Kiume:\n"
        "- Mashati ya kiume (M-L-XL): Tsh 18,000\n"
        "- Gauni za mtoko: Tsh 35,000\n"
        "- T-shirt zenye maandishi: Tsh 15,000\n"
        "🧺 Zipo za cotton, polyester, na denim."
    )

# /viatu
async def viatu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👟 Viatu vya kisasa:\n"
        "- Sneakers za kiume: Tsh 45,000\n"
        "- Heels za kike: Tsh 50,000\n"
        "- Sandals: Tsh 20,000\n"
        "🌍 Vimeagizwa kutoka Dubai & Turkey."
    )

# /malabo
async def malabo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛋️ Malabo ya ndani:\n"
        "- Carpet kubwa 5x7: Tsh 60,000\n"
        "- Mapazia pair 2: Tsh 35,000\n"
        "- Taa za kisasa: Tsh 25,000\n"
        "🏠 Fanya nyumba yako iwe na mvuto wa kipekee!"
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bidhaa", bidhaa))
    app.add_handler(CommandHandler("simu", simu))
    app.add_handler(CommandHandler("computer", computer))
    app.add_handler(CommandHandler("nguo", nguo))
    app.add_handler(CommandHandler("viatu", viatu))
    app.add_handler(CommandHandler("malabo", malabo))

    print("🤖 Bot inaendelea...")

    app.run_polling()
