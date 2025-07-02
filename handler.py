from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes
from prompts import FIRST_PROMPT, SECOND_PROMPT, ROLE_KEYBOARD
from gemini_api import chat_sessions

async def set_role(update: Update, context: ContextTypes.DEFAULT_TYPE, role_name: str):
    """
    Sets a new role for the chat and resets the context.
    Устанавливает новую роль для чата и сбрасывает контекст.
    """
    chat_id = update.message.chat_id
    model = context.bot_data['gemini_model'] # Get model from bot_data | Получаем модель из bot_data

    # Reset context if chat_id exists | Сброс контекста, если chat_id существует
    if chat_id in chat_sessions:
        del chat_sessions[chat_id]

    confirmation_message = ""
    if role_name == "Creative Storyteller": # NAME OF THE FIRST BUTTON | НАЗВАНИЕ ПЕРВОЙ КНОПКИ
        chat_sessions[chat_id] = model.start_chat(history=FIRST_PROMPT)
        confirmation_message = "Hi! I am Creative Storyteller. How can I help you?"  # role selection confirmation message | сообщение, подтверждающее выбор роли
    elif role_name == "Technical Assistant": # NAME OF THE SECOND BUTTON | НАЗВАНИЕ ВТОРОЙ КНОПКИ
        chat_sessions[chat_id] = model.start_chat(history=SECOND_PROMPT)
        confirmation_message = "Hi! I am Technical Assistant. How can I help you?"  # role selection confirmation message | сообщение, подтверждающее выбор роли
    else:
        confirmation_message = "Unknown role. Please choose from the suggested ones."
        await update.message.reply_text(confirmation_message, reply_markup=ROLE_KEYBOARD)
        return

    await update.message.reply_text(
        confirmation_message,
        reply_markup=ROLE_KEYBOARD # Return the keyboard | Возвращаем клавиатуру
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Sends a welcome message and instructions upon /start command.
    Отправляет приветственное сообщение и инструкцию по команде /start.
    """
    chat_id = update.message.chat_id
    model = context.bot_data['gemini_model'] # Get model from bot_data | Получаем модель из bot_data

    if model:
        # Initialize with Creative Storyteller by default | Инициализируем с Творческим Рассказчиком по умолчанию
        chat_sessions[chat_id] = model.start_chat(history=FIRST_PROMPT)
        await update.message.reply_text( # /start command message | сообщение команды /start
            'Hello! I am your multi-role AI assistant. \n\n'
            '• In **private chats**, I respond to all your messages.\n'
            '• In **groups**, I respond if you @mention me or reply to my message.\n\n'
            'You can find my source code and create your own bot on [GitHub](YOUR_GITHUB_REPOSITORY_LINK_HERE).\n\n' 
            'Please select a role:',
            reply_markup=ROLE_KEYBOARD # Display buttons on start | Отображаем кнопки при старте
        )
        print(f"New chat created for chat_id: {chat_id}.")
    else:
        await update.message.reply_text('Sorry, the service is temporarily unavailable due to a configuration error.')


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Main message handler.
    Responds to messages in private chats, mentions, and replies to the bot in groups.
    Also handles role selection button presses.
    Главный обработчик сообщений.
    Реагирует на сообщения в ЛС, на упоминания и на ответы боту в группах.
    Также обрабатывает нажатия на кнопки выбора роли.
    """
    model = context.bot_data['gemini_model'] # Get model from bot_data | Получаем модель из bot_data
    if not model:
        await update.message.reply_text('Sorry, the service is temporarily unavailable.')
        return

    chat_id = update.message.chat_id
    user_input = update.message.text

    # Handle button presses | Обработка нажатий на кнопки
    if user_input == "Creative Storyteller": # NAME OF THE FIRST BUTTON | НАЗВАНИЕ ПЕРВОЙ КНОПКИ
        await set_role(update, context, "Creative Storyteller") # Pass button text as role name | Передаем текст кнопки как имя роли
        return
    elif user_input == "Technical Assistant": # NAME OF THE SECOND BUTTON | НАЗВАНИЕ ВТОРОЙ КНОПКИ
        await set_role(update, context, "Technical Assistant") # Pass button text as role name | Передаем текст кнопки как имя роли
        return

    # Determine if the bot should respond | Определяем, должен ли бот отвечать
    should_respond = False
    is_group = update.message.chat.type in ['group', 'supergroup']

    if not is_group:
        should_respond = True
    else:
        bot_username = f"@{context.bot.username}"
        if bot_username in user_input:
            should_respond = True
            user_input = user_input.replace(bot_username, "").strip()

        if update.message.reply_to_message and update.message.reply_to_message.from_user.id == context.bot.id:
            should_respond = True

    if not should_respond:
        return

    if not user_input:
        await update.message.reply_text("Слушаю вас! | I'm listening!", reply_to_message_id=update.message.message_id)
        return

    # Get or create a chat session. If no session, initialize Creative Storyteller.
    # Получаем или создаем сессию чата. Если сессии нет, инициализируем Творческого Рассказчика.
    if chat_id not in chat_sessions:
        chat_sessions[chat_id] = model.start_chat(history=FIRST_PROMPT)
        print(f"New chat created for chat_id: {chat_id}.")

    try:
        response = chat_sessions[chat_id].send_message(user_input)
        await update.message.reply_text(response.text, reply_to_message_id=update.message.message_id)
    except Exception as e:
        print(f"Error communicating with Gemini API: {e}")
        await update.message.reply_text('An error occurred, please try again later.')
