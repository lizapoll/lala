#!/usr/bin/env python

import telebot
import random
from telebot.types import Message

TOKEN = '731167915:AAGWcrd09zSlEwpphUANLHctvDQSDd_ImN8'
STICKER_ID = 'AAQCABNMIEsNAASK5sIu9T23a2RdAQABAg'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands = ['start', 'help'])
def command_handler(message: Message):
  bot.reply_to(message, 'Hi boy')

@bot.message_handler(content_types = ['text'])
@bot.edited_message_handler(content_types=['text']) 
def  echo_gigits(message: Message):
  if 'Alex' in message.text:
    bot.reply_to(message, 'YaYa')
    return
  bot.reply_to(message, str(random.random())) 

@bot.message_handler(content_types = ['sticker'])
def sticker_handler(message: Message):
  bot.send_sticker(message.chat.id, STICKER_ID)


bot.polling(timeout = 60)
