import os from telegram import Update from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

bidhaa = { "Simu Aina Zote": "Tunauza simu za aina zote - bei kuanzia TSh 150,000.", "Computer": "Laptops na desktops kwa matumizi ya nyumbani na ofisi.", "Malabo ya Ndani": "Manukato na mafuta ya kupaka ya hali ya juu.", "Nguo za Kiume": "Nguo kali za kisasa kwa wanaume – mashati, suruali na zaidi.", "Nguo za Kike": "Nguo bomba kwa wanawake – magauni, tops, sketi nk.", "Viatu Aina Zote": "Viatu vya kike na kiume – casual, official, sports shoes.", "Cosmetics": "Bidhaa bora za urembo – lipsticks, lotions, skincare nk.", "Dawa za Meno": "Dawa za meno za asili zinazotunza afya ya kinywa.", "Bee Pollen": "Bidhaa ya afya kutoka kwenye asali – kuongeza nguvu na kinga." }

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): msg = ( "Karibu kwenye Zephyr Products Bot \U0001F6CD️\n\n" "Tuma /bidhaa kuona orodha ya bidhaa au /malipo kujua jinsi ya kulipa.\n" ) await update.message.reply_text(msg, parse_mode="Markdown")

async def bidhaa_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE): msg = "\U0001F4E6 Bidhaa Zetu:\n" for name, desc in bidhaa.items(): msg += f"\n\u2728 {name}\n{desc}\n" await update.message.reply_text(msg, parse_mode="Markdown")

async def malipo(update: Update, context: ContextTypes.DEFAULT_TYPE): msg = ( "\U0001F4B3 Malipo yanafanyika kupitia M-Pesa:\n" "0740233767\n" "Tunatuma bidhaa nchi nzima \U0001F1F9\U0001F1FF!\n" ) await update.message.reply_text(msg, parse_mode="Markdown")

app = ApplicationBuilder().token(BOT_TOKEN).build() app.add_handler(CommandHandler("start", start)) app.add_handler(CommandHandler("bidhaa", bidhaa_cmd)) app.add_handler(CommandHandler("malipo", malipo))

app.run_polling()

