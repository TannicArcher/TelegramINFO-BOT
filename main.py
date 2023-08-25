from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Обработчик команды /start
def start(update, context):
    user = update.message.from_user
    chat = update.message.chat

    # Показать информацию о пользователе
    context.bot.send_message(chat_id=chat.id, text=f"ID пользователя: {user.id}")
    context.bot.send_message(chat_id=chat.id, text=f"Имя пользователя: {user.username}")
    context.bot.send_message(chat_id=chat.id, text=f"Имя и фамилия: {user.first_name} {user.last_name}")
    context.bot.send_message(chat_id=chat.id, text=f"Номер телефона: {user.phone_number}")
    context.bot.send_photo(chat_id=chat.id, photo=user.photo)

    # Показать информацию о чате
    context.bot.send_message(chat_id=chat.id, text=f"ID чата: {chat.id}")
    context.bot.send_message(chat_id=chat.id, text=f"Тип чата: {chat.type}")
    context.bot.send_message(chat_id=chat.id, text=f"Название чата: {chat.title}")
    context.bot.send_photo(chat_id=chat.id, photo=chat.photo)

    # Показать информацию о сообщении
    context.bot.send_message(chat_id=chat.id, text=f"ID сообщения: {update.message.message_id}")
    context.bot.send_message(chat_id=chat.id, text=f"Текст сообщения: {update.message.text}")
    context.bot.send_message(chat_id=chat.id, text=f"Дата и время отправки: {update.message.date}")
    context.bot.send_message(chat_id=chat.id, text=f"Информация об отправителе: {user.id}, {user.username}, {user.first_name} {user.last_name}")

# Обработчик команды /user_info
def user_info(update, context):
    user_id = context.args[0]  # Получение ID пользователя из аргументов команды
    user = context.bot.get_chat(user_id)

    # Показать информацию о пользователе
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"ID пользователя: {user.id}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Имя пользователя: {user.username}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Имя и фамилия: {user.first_name} {user.last_name}")
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Номер телефона: {user.phone_number}")
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=user.photo)

# Создание экземпляра бота с токеном вашего бота
updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

# Получение диспетчера для регистрации обработчиков
dispatcher = updater.dispatcher

# Регистрация обработчиков команды /start и /user_info
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('user_info', user_info))

# Запуск бота
updater.start_polling()
