#!/usr/bin/python

from telebot.async_telebot import AsyncTeleBot
from telebot import asyncio_filters
import json

settings_file = open("settings.json")
settings_json = json.load(settings_file)
bot = AsyncTeleBot(settings_json["token"])

welcome_message = "Привет, {}! Добро пожаловать на канал {}! Прочти пожалуйста следующие правила!!!"
bye_message = "До скорой встречи, {}! Всегда тебе рады!!!"

@bot.message_handler(content_types=["new_chat_members"])
async def say_hello(message):
    await bot.reply_to(message, welcome_message.format(message.json['from']['first_name'] + " " + message.json['from']['last_name'], message.json['chat']['title']))

@bot.message_handler(content_types=["left_chat_member"])
async def say_bye(message):
    await bot.reply_to(message, bye_message.format(message.json['from']['first_name'] + " " + message.json['from']['last_name']))

@bot.message_handler(chat_types=['supergroup'], is_chat_admin=True, commands=["welcome"])
async def change_welcome(message):
    global welcome_message
    if (len(message.text.replace("/welcome ", "")) > 0 and  len(message.text.replace("/welcome ", "")) < 4999):
        welcome_message = message.text.replace("/welcome ", "")
        await bot.send_message(message.chat.id, welcome_message)

@bot.message_handler(chat_types=['supergroup'], is_chat_admin=True, commands=["bye"])
async def change_bye(message):
    global bye_message
    if (len(message.text.replace("/bye ", "")) > 0 and len(message.text.replace("/bye ", "")) < 4999):
        bye_message = message.text.replace("/bye ", "")
        await bot.send_message(message.chat.id, bye_message)

# Register filter
bot.add_custom_filter(asyncio_filters.IsAdminFilter(bot))

import asyncio
asyncio.run(bot.polling())