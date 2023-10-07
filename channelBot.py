#!/usr/bin/python

from telebot.async_telebot import AsyncTeleBot
import json

settings_file = open("settings.json")
settings_json = json.load(settings_file)
bot = AsyncTeleBot(settings_json["token"])

# Handle '/start' and '/help'
@bot.channel_post_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.channel_post_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

import asyncio
asyncio.run(bot.polling())