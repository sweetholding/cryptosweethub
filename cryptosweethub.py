
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ConversationHandler, ContextTypes, filters

TOKEN = "7533223527:AAG5H3gOnEXJX_rgQ3PKQ4rss224pMpbrJ0"

MENU, PRODUCT, PAYMENT = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["lang"] = "ua"
    menu_buttons = [["🔹 Підписатись безкоштовно на канал"], ["🔹 Дізнатися про навчання та заробіток"]]
    await update.message.reply_text(
        "✅ Вітаємо у головному меню!",
        reply_markup=ReplyKeyboardMarkup(menu_buttons, resize_keyboard=True)
    )
    return MENU

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "безкоштовно" in text:
        await update.message.reply_text("👉 Переходь до нашого Telegram-каналу: @Crypto_Sweet")
        return MENU

    if "навчання" in text:
        options = [["🧠 Відеоуроки + комʼюніті (150$)"],
                   ["💬 Доступ до комʼюніті без уроків (1000 грн)"],
                   ["🚀 Індивідуальне навчання"]]
        await update.message.reply_text(
            "Ось формати участі, обери що тобі ближче:",
            reply_markup=ReplyKeyboardMarkup(options, resize_keyboard=True, one_time_keyboard=True)
        )
        return PRODUCT

async def product_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "Відеоуроки" in text:
        message = """📥 *Відеоуроки + доступ в комʼюніті (150$)*

✅ *Цей курс для тебе, якщо:*  
🔥 Хочеш почати заробляти на крипті, але не знаєш, з чого почати  
🔥 Втомився дивитись відео на YouTube, де нічого не зрозуміло  
🔥 Потрібен чіткий план + підтримка досвідчених трейдерів  

➡️ *Ти отримаєш:*  
✅ Повний гайд по криптовалюті від нуля до перших прибутків  
✅ Реальні приклади заробітку з поясненням стратегії  
✅ Готові інструменти, які дозволяють копіювати великі угоди  
✅ 24/7 підтримку в ком’юніті (відповімо на всі питання)  

🎯 *Як це працює?*  
✅ Олег, 34 роки, до навчання нічого не розумів у трейдингу та криптовалюті.  
За час навчання заробив майже $10,000!  
📸 Дивись його кейс: [Instagram](https://www.instagram.com/reel/Cnjbm_RKDJC/?igsh=engxNnBtbDIwZG81)  

💳 *Обери спосіб оплати:*"""

    elif "Доступ до комʼюніті" in text:
        message = """💬 *Доступ в комʼюніті без уроків (1000 грн / міс)*  

✅ *Що таке наше ком’юніті?*  
🔥 Закрита група для заробітку  
🚀 Ексклюзивні ідеї, які не знайти у відкритому доступі  
👀 Моніторинг великих угод (бачимо, що купують великі фонди)  
🎯 Щоденні торгові сигнали – що купувати/продавати  
🧠 Живі Zoom-зустрічі з експертами  

🦾 *Ексклюзивний бонус:*  
💡 Ти отримаєш доступ до унікальних Telegram-ботів, які аналізують ринок  
🔍 Бот автоматично відстежує важливі транзакції та надсилає тобі сигнал  
📩 Це економить час – тобі не потрібно самостійно аналізувати ринок!  

✅ Будь активним – і залишишся в ком’юніті назавжди БЕЗКОШТОВНО  

💳 *Обери спосіб оплати:*"""

    elif "Індивідуальне" in text:
        message = """🚀 *Індивідуальне навчання – 100% персоналізований підхід*  

💡 Хочеш, щоб тебе особисто навчили заробляти?  
✅ Ми підберемо кращу стратегію саме для тебе  
✅ Навчимо аналізувати ринок, макроекономіку, тренди  
✅ Ти дізнаєшся, коли купувати/продавати активи  

📊 *Реальний кейс:*  
🎓 Одна з наших учениць почала з нуля і вже стабільно заробляє на крипті  
📈 Вона пройшла весь шлях – від перших угод до постійного доходу  
📸 Дивись її історію: [Instagram](https://www.instagram.com/reel/DE0VlQWtoxC/?igsh=ZHZ3dzBzeWF0aGQ0)  
🎥 Ось відео з нею: [YouTube](https://youtu.be/GMbS6vTaGks?si=P-tOwZ-9RNBl3He4)  

✍️ Напиши прямо сюди або звернись в @SBbrend — підберемо варіант під тебе."""

    else:
        return PRODUCT

    await update.message.reply_text(
        message,
        reply_markup=ReplyKeyboardMarkup([
            ["Оплата криптою"], ["Оплата картою"], ["🔙 Назад"]
        ], resize_keyboard=True, one_time_keyboard=True),
        parse_mode="Markdown"
    )
    return PAYMENT


async def handle_payment_method(update: Update, context: ContextTypes.DEFAULT_TYPE):
    choice = update.message.text.strip()

    if "картою" in choice:
        lang = context.user_data.get("lang", "ua")
        if lang == "ru":
            msg = "💳 Для оплаты картой напишите в @SBbrend — вам отправят реквизиты."
        else:
            msg = "💳 Для оплати карткою напишіть у @SBbrend — вам надішлють реквізити."
        await update.message.reply_text(msg, parse_mode="Markdown")
        await update.message.reply_text(
            "🔙 Якщо хочеш змінити спосіб оплати, натисни 'Назад'",
            reply_markup=ReplyKeyboardMarkup([["🔙 Назад"]], resize_keyboard=True)
        )
        return PAYMENT

    elif "криптою" in choice:
        msg = """💸 *Надішли USDT (TRC20) на адресу:*
`TTHyGV5KWETfJvGUvCXnhgUsvMUMus31Zw`

⚠️ *Після оплати надішліть скріншот підтвердження в* @SBbrend"""
        await update.message.reply_text(msg, parse_mode="Markdown")
        await update.message.reply_text(
            "🔙 Якщо хочеш змінити спосіб оплати, натисни 'Назад'",
            reply_markup=ReplyKeyboardMarkup([["🔙 Назад"]], resize_keyboard=True)
        )
        return PAYMENT

    elif "Назад" in choice or "🔙" in choice:
        await update.message.reply_text(
            "🔙 Повертаємось до вибору формату участі...",
            reply_markup=ReplyKeyboardMarkup([
                ["🧠 Відеоуроки + комʼюніті (150$)"],
                ["💬 Доступ до комʼюніті без уроків (1000 грн)"],
                ["🚀 Індивідуальне навчання"]
            ], resize_keyboard=True, one_time_keyboard=True)
        )
        return PRODUCT

    await update.message.reply_text("❗ Невідома команда. Спробуй ще раз.")
    return PAYMENT

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            MENU: [MessageHandler(filters.TEXT & ~filters.COMMAND, menu)],
            PRODUCT: [MessageHandler(filters.TEXT & ~filters.COMMAND, product_info)],
            PAYMENT: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_payment_method)],
        },
        fallbacks=[CommandHandler("start", start)],
    )
    app.add_handler(conv_handler)
    print("🤖 Бот запущен")
    app.run_polling()
