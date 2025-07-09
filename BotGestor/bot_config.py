from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola, soy el asistente virtual de amadeus, cuentame que quieres hacer el dia de hoy " + update.message.text)

def main():
    # Create the bot application
    bot = Application.builder().token("xxxx").build()

    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    bot.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
