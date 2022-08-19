import config

from telebot import types
from utils.FileUtils import writeFile


def make_button(bot, message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_yes, key_no)
    bot.send_message(message.from_user.id, text="Хочешь получать напоминания от меня?", reply_markup=keyboard)


def add_chat(chats, chat_id, chat_list):
    if chat_id in chat_list:
        if chat_list[chat_id]:
            print(f"Пользователь {chat_id} уже в очереди")
        else:
            chat_list.update({chat_id: True})
            print(f"Пользователь {chat_id} добавлен в очередь")
            writeFile(config.dataSet, chats)
    else:
        print(f"Пользователь {chat_id} не нажимал /start или как вообще его нет в списках")


def del_chat(chats, chat_id, chat_list):
    if chat_id in chat_list:
        if not chat_list[chat_id]:
            print(f"Пользователь {chat_id} уже отписан")
        else:
            chat_list.update({chat_id: False})
            print(f"Пользователь {chat_id} отписался")
            writeFile(config.dataSet, chats)


def send_notification(bot, chat):
    if True:
        for i in chat.keys():
            if chat.get(i):
                ret_msg = bot.send_message(i, "А ты заказал еду?")
                assert ret_msg.message_id
                print(f"Уведомление {i} отправлено")
    # else:
    #     print("еще не время")
