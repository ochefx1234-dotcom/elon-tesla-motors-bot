
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, ContextTypes, filters
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚘 Explore Vehicles", callback_data="vehicles")],
        [InlineKeyboardButton("💰 Payment Calculator", callback_data="payment")],
        [InlineKeyboardButton("📦 Track Order", callback_data="tracking")],
        [InlineKeyboardButton("🚗 Book Test Drive", callback_data="testdrive")],
        [InlineKeyboardButton("🤖 AI Vehicle Assistant", callback_data="assistant")],
        [InlineKeyboardButton("🌍 Select Country", callback_data="country")]
    ]

    await update.message.reply_text(
        "Welcome to Elon Tesla Motors!\n\n"
        "Your vehicle information and customer service assistant.\n\n"
        "Please select an option:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    responses = {
        "vehicles": "🚘 Explore our vehicle collection. More vehicle details coming soon.",
        "payment": "💰 Payment calculator will help estimate your monthly payments.",
        "tracking": "📦 Please enter your order reference number.",
        "testdrive": "🚗 Please send your name, country and preferred test-drive date.",
        "assistant": "🤖 Hello! Ask me a question about Tesla vehicles.",
        "country": "🌍 Please enter your country."
    }

    await query.message.reply_text(responses.get(query.data, "Please try again."))

async def messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Thank you for contacting us. Please tell us how we can assist you."
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable is missing")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messages))
    app.run_polling()

if __name__ == "__main__":
    main()
