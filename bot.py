import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from groq import Groq

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

TELEGRAM_TOKEN = "8618916753:AAGycKunJdQTyoKRaYCkpHrB9XFJhd_dp0E"
GROQ_API_KEY = "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"

groq_client = Groq(api_key=GROQ_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello Azhar! GlitchGPT Defensive System Active. Bhejein jo coding sawal aapko troubleshoot karna hai.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        completion = groq_client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful and polite programming assistant. Help the user debug code, analyze standard networking concepts, and fix syntax errors logically."
                },
                {"role": "user", "content": user_text}
            ]
        )
        await update.message.reply_text(completion.choices.message.content)
    except Exception as e:
        logging.error(f"Error: {e}")
        await update.message.reply_text("❌ Server busy hai, dobara try karein.")

def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.run_polling()

if __name__ == '__main__':
    main()
    
