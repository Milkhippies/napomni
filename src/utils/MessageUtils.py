import config, logging

from telebot import types

from utils.FileUtils import writeFile
from utils.ImageAPI import getImageURL


def make_button(bot, message):
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_yes, key_no)
    bot.send_message(message.from_user.id, text="Хочешь получать напоминания от меня?", reply_markup=keyboard)


def add_chat(chats, chat_id):
    if chat_id in chats:
        if chats[chat_id]:
            logging.info(f"User {chat_id} are in list")
        else:
            chats.update({chat_id: True})
            logging.info(f"User {chat_id} added in list")
            writeFile(config.dataSet, chats)
    else:
        logging.info(f"User {chat_id} not started bot, not found in list")


def del_chat(chats, chat_id):
    if chat_id in chats:
        if not chats[chat_id]:
            logging.info(f"User {chat_id} are unsubscribed")
        else:
            chats.update({chat_id: False})
            logging.info(f"User {chat_id} unsubscribed")
            writeFile(config.dataSet, chats)


def send_notification(bot, chat):
    if True:
        for i in chat.keys():
            if chat.get(i):
                send_notif(bot, i, "А ты заказал еду?")
                send_img(bot, i)
                logging.info(f"Notification for {i} sent successfully")
    # else:
    #     print("еще не время")


def send_notif(bot, i, text):
    try:
        bot.send_message(i, text)
    except Exception:
        logging.error(f'Error with send notification {i}')
    finally:
        logging.info(f'Text for {i} sent successfully')


def send_img(bot, i):
    try:
        url = getImageURL(config.catURL, config.catKEY)
        bot.send_photo(i, url)
    except Exception:
        logging.error(f'Error with img for {i}')
    finally:
        logging.info(f'Image for {i} sent successfully')

