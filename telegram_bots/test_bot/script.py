import telebot
import config
import random

from telebot import types 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def greeting(message):
    sticker = open('stickers/laugh.tgs', 'rb')
    bot.send_sticker(message.chat.id, sticker)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Random Number")
    item2 = types.KeyboardButton("😁 How're u doing?")
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Hello, {0}!\nI am a dumbass bot called IDontRememberItsNameSorry.\nUsing this bot you can do <b>COMPLETELY NOTHING!</b>. <i>Get the fuck outta here</i>'.format(message.chat.first_name), parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def talk(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Random Number':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == "😁 How're u doing?":
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Good!", callback_data='good')
            item2 = types.InlineKeyboardButton("Bad...", callback_data='bad')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, '<b>Great!</b> How about you?', parse_mode='html', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'You have entered a command I dont know you stupid dumbass')

bot.polling(none_stop=True)