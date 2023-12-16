import telebot

token='6947114833:AAFBU8bHQxKCRfqhu6ZNUwNdnLgr9aYWtW4'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Добро пожаловать в мой первый бот-визитку!\nЭтот бот может рассказать об моих увлечениях и жизни\nПредлагаю ознакомиться с командами /help!")

@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, "/start - Запускает бота\n/help - Поможет разобраться с командами бота и как их использовать\n/aboutme - справочная информация обо мне)))")

@bot.message_handler(commands=['aboutme'])
def handle_aboutme(message):
    photo1 = open('about-me.jpg', 'rb')
    photo2 = open('photo2.jpg', 'rb')
    photo3 = open('photo3.jpg', 'rb')

    bot.send_photo(message.chat.id, photo1)
    bot.send_photo(message.chat.id, open('photo2.jpg', 'rb'))
    bot.send_photo(message.chat.id, open('photo3.jpg', 'rb'))
    bot.send_message(message.chat.id, "Ещё раз привет! Меня зовут Оля и тут будет находиться information обо мне)\nЯ живу в Москве. Мне 13 лет, 31 декабря исполнится 14!!! Я люблю кодить на питоне, рисовать, я очень творческая личность. Сейчас ещё обучаюсь web-дизайну и в будущем хочу стать им. А здесь хочу научиться создавать ботов и радовать всех своими ботами)")
    photo4 = open('monika.jpg', 'rb')
    bot.send_photo(message.chat.id, photo4)
    bot.send_message(message.chat.id, "А так же у меня есть очень милая морская свинка, которая появилась у меня в сентябре")

bot.polling()