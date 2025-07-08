# gemini-telegram-bot
Telegram Bot with Gemini AI (Multi-Role Support)

This repository contains the code for a Telegram bot that leverages the Google Gemini AI to provide responses based on various customizable roles. Users can interact with the bot in private chats or groups (by mentioning the bot or replying to its messages) and switch between the available roles using inline keyboard buttons.

## Features:
* **Multi-Role Support:** Easily define and switch between different AI personas.
* **Contextual Conversations:** The bot maintains chat history for each user, allowing for more coherent and continuous conversations within the chosen persona.
* **Group Chat Support:** The bot can operate in Telegram groups, responding when mentioned or replied to.
* **Modular Codebase:** The project is structured into multiple Python files for better organization and maintainability.
* **Environment Variable Configuration:** API tokens are securely loaded from environment variables.

## Customization and Configuration:
This bot is designed to be easily customizable. Here's where you can make changes:

* **`prompts.py`**
    * **`FIRST_PROMPT`, `SECOND_PROMPT`**: These are the core AI personas. You can completely rewrite the content within the `parts` array for both the `user` and `model` roles to define new behaviors, knowledge bases, and interaction styles for your AI.
    * **`ROLE_KEYBOARD`**: Modify the `KeyboardButton` texts (e.g., `"Creative Storyteller"`, `"Technical Assistant"`) to change the names displayed on the role selection buttons in Telegram.
    * **`one_time_keyboard`**: Set to `True` if you want the keyboard to disappear after a selection, or `False` if you want it to remain visible.

* **`handler.py`**
    * **`set_role` function**:
        * Update the `if/elif` conditions (`if role_name == "Creative Storyteller":`) if you changed the button names in `prompts.py`.
        * Modify `confirmation_message` for each role to provide a custom welcome message when a user selects that role.
        * Adjust the default role initialized in `start` function (`chat_sessions[chat_id] = model.start_chat(history=FIRST_PROMPT)`) if you want a different default starting persona.
    * **`start` function**: Customize the main welcome message (`Hello! I am your multi-role AI assistant...`) to fit your bot's personality.
    * **`handle_message` function**: Update the `if/elif` conditions (`if user_input == "Creative Storyteller":`) to match any changes made to the button names in `prompts.py`.

* **`gemini_api.py`**
    * **`model = genai.GenerativeModel('gemini-1.5-flash')`**: You can change `'gemini-1.5-flash'` to a different Gemini model if you prefer, based on availability and your needs (e.g., `gemini-pro`, `gemini-1.5-pro`). Refer to the official Gemini API documentation for available models.

* **`config.py`**
    * This file is where the environment variables `TELEGRAM_TOKEN` and `GEMINI_API_KEY` are referenced. You will set these values in your deployment environment, not directly in this file.

* **`main.py`**
    * This is the main entry point for the bot. While you generally won't need to edit this file, it's where the Telegram Application is built and handlers are added.

## Setup:
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/FiiiiiiiiiiiiiiiiiiiiiiiiSH/gemini-telegram-bot.git
    cd gemini-telegram-bot
    ```
2.  **Install dependencies:**
    ```bash
    pip install python-telegram-bot google-generativeai
    ```
3.  **Set environment variables:**
    Obtain your Telegram Bot Token from BotFather and your Gemini API Key from Google AI Studio. Then set them as environment variables in your operating system or hosting environment (e.g., PythonAnywhere, Heroku):
    ```bash
    export TELEGRAM_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
    export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
    ```
    (For Windows, use `set` instead of `export` in Command Prompt, or `$env:VARIABLE="VALUE"` in PowerShell).

4.  **Run the bot:**
    ```bash
    python main.py
    ```

## Usage:
* Start a chat with your bot on Telegram and send the `/start` command.
* Select your desired role using the provided keyboard buttons.
* In private chats, simply type your message.
* In group chats, mention the bot (e.g., `@YourBotUsername Your message`) or reply directly to one of its messages.

## License:
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

# Telegram Бот с Gemini AI (Поддержка Мульти-Ролей)

Этот репозиторий содержит код Telegram-бота, который использует Google Gemini AI для предоставления ответов на основе различных настраиваемых ролей. Пользователи могут взаимодействовать с ботом в личных чатах или группах (упоминая бота или отвечая на его сообщения) и переключаться между доступными ролями с помощью кнопок встроенной клавиатуры.

## Особенности:
* **Поддержка мульти-ролей:** Легко определяйте и переключайтесь между различными персонами ИИ.
* **Контекстные беседы:** Бот сохраняет историю чата для каждого пользователя, что позволяет вести более связные и непрерывные беседы в рамках выбранной персоны.
* **Поддержка групповых чатов:** Бот может работать в группах Telegram, отвечая на упоминания или ответы на его сообщения.
* **Модульная кодовая база:** Проект структурирован на несколько файлов Python для лучшей организации и удобства поддержки.
* **Конфигурация через переменные окружения:** Токены API безопасно загружаются из переменных окружения.

## Настройка и Конфигурация:
Этот бот разработан таким образом, чтобы его было легко настраивать. Вот где вы можете внести изменения:

* **`prompts.py`**
    * **`FIRST_PROMPT`, `SECOND_PROMPT`**: Это основные персоны ИИ. Вы можете полностью переписать содержимое в массиве `parts` как для роли `user`, так и для роли `model`, чтобы определить новое поведение, базы знаний и стили взаимодействия для вашего ИИ.
    * **`ROLE_KEYBOARD`**: Измените тексты `KeyboardButton` (например, `"Creative Storyteller"`, `"Technical Assistant"`), чтобы изменить названия, отображаемые на кнопках выбора роли в Telegram.
    * **`one_time_keyboard`**: Установите значение `True`, если вы хотите, чтобы клавиатура исчезала после выбора, или `False`, если вы хотите, чтобы она оставалась видимой.

* **`handler.py`**
    * **Функция `set_role`**:
        * Обновите условия `if/elif` (`if role_name == "Creative Storyteller":`), если вы изменили названия кнопок в `prompts.py`.
        * Измените `confirmation_message` для каждой роли, чтобы предоставить пользовательское приветственное сообщение, когда пользователь выбирает эту роль.
        * Настройте роль по умолчанию, инициализируемую в функции `start` (`chat_sessions[chat_id] = model.start_chat(history=FIRST_PROMPT)`), если вы хотите другую персону по умолчанию при запуске.
    * **Функция `start`**: Настройте основное приветственное сообщение (`Hello! I am your multi-role AI assistant...`), чтобы оно соответствовало индивидуальности вашего бота.
    * **Функция `handle_message`**: Обновите условия `if/elif` (`if user_input == "Creative Storyteller":`), чтобы они соответствовали любым изменениям, внесенным в названия кнопок в `prompts.py`.

* **`gemini_api.py`**
    * **`model = genai.GenerativeModel('gemini-1.5-flash')`**: Вы можете изменить `'gemini-1.5-flash'` на другую модель Gemini, если хотите, в зависимости от доступности и ваших потребностей (например, `gemini-pro`, `gemini-1.5-pro`). См. официальную документацию Gemini API для доступных моделей.

* **`config.py`**
    * Этот файл содержит ссылки на переменные окружения `TELEGRAM_TOKEN` и `GEMINI_API_KEY`. Вы будете устанавливать эти значения в вашей среде развертывания, а не непосредственно в этом файле.

* **`main.py`**
    * Это основная точка входа для бота. Хотя обычно вам не потребуется редактировать этот файл, именно здесь создается приложение Telegram и добавляются обработчики.

## Настройка:
1.  **Клонируйте репозиторий:**
    ```bash
    git clone https://github.com/FiiiiiiiiiiiiiiiiiiiiiiiiSH/gemini-telegram-bot.git
    cd gemini-telegram-bot
    ```
2.  **Установите зависимости:**
    ```bash
    pip install python-telegram-bot google-generativeai
    ```
3.  **Установите переменные окружения:**
    Получите ваш Telegram Bot Token у BotFather и ваш Gemini API Key из Google AI Studio. Затем установите их как переменные окружения в вашей операционной системе или среде хостинга (например, PythonAnywhere, Heroku):
    ```bash
    export TELEGRAM_TOKEN="ВАШ_ТОКЕН_ТЕЛЕГРАМ_БОТА"
    export GEMINI_API_KEY="ВАШ_КЛЮЧ_API_GEMINI"
    ```
    (Для Windows используйте `set` вместо `export` в командной строке, или `$env:VARIABLE="VALUE"` в PowerShell).

4.  **Запустите бота:**
    ```bash
    python main.py
    ```

## Использование:
* Начните чат с вашим ботом в Telegram и отправьте команду `/start`.
* Выберите желаемую роль с помощью предоставленных кнопок клавиатуры.
* В личных чатах просто введите свое сообщение.
* В групповых чатах упомяните бота (например, `@ИмяВашегоБота Ваше сообщение`) или ответьте непосредственно на одно из его сообщений.

## Лицензия:
Этот проект распространяется под лицензией MIT. Подробности см. в файле `LICENSE`.
"""
