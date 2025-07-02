import os
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN, GEMINI_API_KEY
from gemini_api import initialize_gemini_model, chat_sessions
from handlers import start, handle_message

def main():
    """
    Main function to run the bot.
    Основная функция для запуска бота.
    """
    # Check if API tokens are available | Проверяем наличие токенов API
    if not TELEGRAM_TOKEN or not GEMINI_API_KEY:
        print("Error: TELEGRAM_TOKEN or GEMINI_API_KEY not found in environment variables.")
        return

    # Initialize Gemini model | Инициализируем модель Gemini
    model = initialize_gemini_model(GEMINI_API_KEY)
    if not model:
        print("Gemini model could not be initialized. Exiting.")
        return

    print("Bot is running!")
    # Build the Telegram Application | Создаем приложение Telegram
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Pass the model to handlers context | Передаем модель в контекст обработчиков
    application.bot_data['gemini_model'] = model
    application.bot_data['chat_sessions'] = chat_sessions

    # Add handlers | Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot | Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()