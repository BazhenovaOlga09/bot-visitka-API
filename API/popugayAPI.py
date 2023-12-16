import telebot

token='6876940057:AAGIv1BaDnOWSBkJ-VseLHodR_caCSiCN6g'
bot=telebot.TeleBot(token)

def filter_hello(message):
    words = ["привет", "хай", "ку"]
    return any(map(lambda word: word in message.text.lower(), words))

def filter_password(message):
    password = "привет"
    return password in message.text

@bot.message_handler(content_types=['text'], func = filter_password)
def say_hello(message):
    bot.send_message(message.chat.id, "Здравствуй!")


def filter_password(message):
    password = "пока"
    return password in message.text

@bot.message_handler(content_types=['text'], func = filter_password)
def say_hello(message):
    bot.send_message(message.chat.id, "До встречи!!!")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет это мой первый бот в телеграмме!!!Предлагаю ознакомиться с командами /help!")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "/start - запускает бота\n/help - поможет разобраться с командами")

bot.polling()
