from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bidhaa zinazopatikana
BIDHAA = """
📦 *Bidhaa Zilizopo:*
- 📱 Simu Aina Zote  
- 💻 Computer  
- 🧴 Malabo ya Ndani  
- 👔 Nguo za Kiume  
- 👗 Nguo za Kike  
- 👟 Viatu Aina Zote  
- 💄 Cosmetics  
- 🪥 Dawa za Meno  
- 🍯 Bee Pollen  
"""

MALIPO = """
💳 *Jinsi ya Kulipa:*

Lipa kwa M-Pesa kupitia namba: *0740233767*

✅ Baada ya malipo, tuma risiti yako kwa Telegram au WhatsApp ili uthibitishiwe.

🌍 Tunatuma bidhaa nchi nzima 🇹🇿
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Karibu kwenye *Zephyr Products Bot!* 🛍️\n\nTuma amri:\n"
        "/bidhaa - kuona bidhaa\n"
        "/malipo - maelezo ya malipo",
        parse_mode="Markdown"
    )

async def bidhaa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(BIDHAA, parse_mode="Markdown")

async def malipo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(MALIPO, parse_mode="Markdown")

if __name__ == '__main__':
    import os

    TOKEN = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bidhaa", bidhaa))
    app.add_handler(CommandHandler("malipo", malipo))

    app.run_polling()
