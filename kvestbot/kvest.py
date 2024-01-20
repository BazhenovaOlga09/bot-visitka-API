import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from infobotkv import plan_action, items, items_dissert, items_swamp, items_cave
from config import token3


bot = telebot.TeleBot(token3)


players = {}

scores = {

}

x = {}
item = {}


def char(message):
    return x.get(message.chat.id) == "char"

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Уже интересно что будет дальше)))'))
    bot.send_photo(message.chat.id, open('../API/рюкзак.png', 'rb'), caption=f"Привет, {message.from_user.first_name}! Готов погрузиться в мир путешествий с разными героями? Если да, то погналии...\nЗдесь ты будешь выбирать героев и их предметы, а в зависимости от выбора местности твое путешествие может закончиться нахождением сокровища или не совсем хорошо....", reply_markup=markup)
    item[message.chat.id] = {"item": ""}
    user_id = message.from_user.id
    players[user_id] = user_id
    players[user_id] = {'level': 1, 'name': message.from_user.first_name}

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Здесь будут перечисленны все команды и их описание\n"
                                      "/start - запуск бота\n"
                                      "/again - пройти бота ещё раз\n"
                                      "/help - поможет разобраться с командами")

@bot.message_handler(commands=['again'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton('Дальше)))'))
    bot.send_photo(message.chat.id, open('../API/рюкзак.png', 'rb'), caption=f"{message.from_user.first_name} захотел пройти квест еще раз? Окей)", reply_markup=markup)
    item[message.chat.id] = {"item": ""}
    user_id = message.from_user.id
    players[user_id] = user_id
    players[user_id] = {'level': 1, 'name': message.from_user.first_name}


@bot.message_handler()
def description(message):
    user_id = message.from_user.id

    if message.text in items:

        item[message.chat.id] = {"item":message.text}

    if message.text == 'Принцесса Эмеральда':
        prins = ReplyKeyboardMarkup(resize_keyboard=True)
        prins.add(KeyboardButton('Лук(оружие)'))
        prins.add(KeyboardButton('Бутылка воды'))
        prins.add(KeyboardButton('Канат'))
        bot.send_photo(message.chat.id, open('../API/Emeralda.png', 'rb'), caption=plan_action["2"])
        bot.send_message(message.chat.id, plan_action["5"], reply_markup=prins)


    elif message.text == "Колдун Блекторн":
        black = ReplyKeyboardMarkup(resize_keyboard=True)
        black.add(KeyboardButton('Шлем'))
        black.add(KeyboardButton('Кактус'))
        black.add(KeyboardButton('Волшебная палочка'))
        bot.send_photo(message.chat.id, open('../API/blacktorn.png', 'rb'), caption=plan_action["3"])
        bot.send_message(message.chat.id, plan_action["5"], reply_markup=black)

    elif message.text == "Мастер Джон":
        mas = ReplyKeyboardMarkup(resize_keyboard=True)
        mas.add(KeyboardButton('Меч'))
        mas.add(KeyboardButton('Фильтр'))
        mas.add(KeyboardButton('Сапоги'))
        bot.send_photo(message.chat.id, open('../API/jon.png', 'rb'), caption=plan_action["4"])
        bot.send_message(message.chat.id, plan_action["5"], reply_markup=mas)
    elif message.text == 'Уже интересно что будет дальше)))' or message.text == 'Дальше)))':
        players[user_id]["level"] = 2
        a = ReplyKeyboardMarkup(resize_keyboard=True)
        a.add(KeyboardButton('Принцесса Эмеральда'))
        a.add(KeyboardButton('Колдун Блекторн'))
        a.add(KeyboardButton('Мастер Джон'))
        bot.send_photo(message.chat.id, open('../API/люди.png', 'rb'), caption=plan_action["1"], reply_markup=a)
    elif message.text == "Пустыни Египта":
        remove_keyboard = types.ReplyKeyboardRemove()
        if item[message.chat.id]["item"] in items_dissert:
            bot.send_photo(message.chat.id, open('../API/dissert.png', 'rb'), caption=plan_action["7"], reply_markup=remove_keyboard)
        elif item[message.chat.id]["item"] == "Бутылка воды":
            bot.send_photo(message.chat.id, open('../API/dissert.png', 'rb'), caption=plan_action["8"], reply_markup=remove_keyboard)
        elif item[message.chat.id]["item"] == "Кактус":
            bot.send_photo(message.chat.id, open('../API/dissert.png', 'rb'), caption=plan_action["9"], reply_markup=remove_keyboard)
        elif item[message.chat.id]["item"] == "Фильтр":
            bot.send_photo(message.chat.id, open('../API/dissert.png', 'rb'), caption=plan_action["10"], reply_markup=remove_keyboard)
        bot.send_message(message.chat.id, "Если хочешь пройти игру заново нажми /again")


    elif message.text == "Болото Бабы Яги":
        remove_keyboard = types.ReplyKeyboardRemove()
        if item[message.chat.id]["item"] in items_swamp:
            bot.send_photo(message.chat.id, open('../API/swamp.png', 'rb'), caption=plan_action["11"], reply_markup=remove_keyboard)
        elif item[message.chat.id]["item"] == "Канат":
            bot.send_photo(message.chat.id, open('../API/swamp.png', 'rb'), caption=plan_action["12"], reply_markup=remove_keyboard)
        elif item[message.chat.id]["item"] == "Сапоги":
            bot.send_photo(message.chat.id, open('../API/swamp.png', 'rb'), caption=plan_action["14"], reply_markup=remove_keyboard)
        elif item[message.chat.id]["item"] == "Волшебная палочка":
            bot.send_photo(message.chat.id, open('../API/swamp.png', 'rb'), caption=plan_action["13"], reply_markup=remove_keyboard)
        bot.send_message(message.chat.id, "Если хочешь пройти игру заново нажми /again")


    elif message.text == "Пещера гоблина":
        remove_keyboard = types.ReplyKeyboardRemove()
        if item[message.chat.id]["item"] in items_cave:
            bot.send_photo(message.chat.id, open('../API/cave.png', 'rb'), caption=plan_action["15"], reply_markup=remove_keyboard)
        elif item[message.chat.id]["item"] == "Лук(оружие)":
            bot.send_photo(message.chat.id, open('../API/cave.png', 'rb'), caption=plan_action["16"], reply_markup=remove_keyboard)
        elif item[message.chat.id]["item"] == "Шлем":
            bot.send_photo(message.chat.id, open('../API/cave.png', 'rb'), caption=plan_action["17"], reply_markup=remove_keyboard)
        elif item[message.chat.id]["item"] == "Меч":
            bot.send_photo(message.chat.id, open('../API/cave.png', 'rb'), caption=plan_action["18"], reply_markup=remove_keyboard)
        bot.send_message(message.chat.id, "Если хочешь пройти игру заново нажми /again")
    else:
        players[user_id]["level"] = 3
        travel = ReplyKeyboardMarkup(resize_keyboard=True)
        travel.add(KeyboardButton('Пустыни Египта'))
        travel.add(KeyboardButton('Болото Бабы Яги'))
        travel.add(KeyboardButton('Пещера гоблина'))
        bot.send_photo(message.chat.id, open('../API/place.png', 'rb'), caption=plan_action["6"], reply_markup=travel)






bot.polling()

