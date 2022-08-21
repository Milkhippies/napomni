import telebot

import config

from utils.RepeatedTimer import RepeatedTimer
from utils.FileUtils import openFile, writeFile

import utils.MessageUtils as smessage

bot = telebot.TeleBot(config.token)
chats = openFile(config.dataSet)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global chats
    bot.send_message(message.from_user.id, "Привет, этот бот для напоминаний")
    smessage.make_button(bot, message)
    chats.update({str(message.from_user.id): False})
    print(f"Новый пользователь - {message.from_user.id}")
    writeFile(config.dataSet, chats)


@bot.message_handler(chat_types=['group'])
def start_in_group(message):
    global chats
    if message.text == "Котик шпротик":
        bot.send_message(message.chat.id, 'сернур')
        chats.update({message.chat.id: True})
        print(f"Группа {message.chat.id} добавлена в очередь")
        writeFile(config.dataSet, chats)


@bot.message_handler(commands=['settings'])
def send_settings(message):
    bot.send_message(message.from_user.id, "Ты в настройках")
    smessage.make_button(bot, message)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global chats
    callback = call
    if callback.data == "yes":
        bot.send_message(callback.message.chat.id, "Отлично, жди оповещения. \nЕсли передумал, зайди в /settings")
        smessage.add_chat(chats, str(callback.message.chat.id))
    elif callback.data == "no":
        bot.send_message(callback.message.chat.id, 'Не очень и хотелось :с \nЕсли передумал, зайди в /settings ')
        smessage.del_chat(chats, str(callback.message.chat.id))


rt = RepeatedTimer(60, smessage.send_notification, bot, chats)

try:
    bot.polling(none_stop=True, interval=0)
finally:
    rt.stop()
