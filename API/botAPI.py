import telebot

# вставь сюда свой токен
token = "6876940057:AAGIv1BaDnOWSBkJ-VseLHodR_caCSiCN6g"

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)

# вставь сюда свой chat_id
chat_id = 5728690151

# отправляем сообщение
bot.send_dice(chat_id)