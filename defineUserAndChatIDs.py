#!/usr/bin/python

from telebot.async_telebot import AsyncTeleBot
import json

settings_file = open("settings.json")
settings_json = json.load(settings_file)
bot = AsyncTeleBot(settings_json["token"])
@bot.message_handler(commands=['myID'])
async def my_id(message):
    await bot.reply_to(message, "Your id is " + str(message.json['from']['id']))

@bot.message_handler(commands=['myChatID'])
async def my_id(message):
    await bot.reply_to(message, "Your chat id is " + str(message.json['chat']['id']))

import asyncio
asyncio.run(bot.polling())