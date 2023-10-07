#!/usr/bin/python

from telebot.async_telebot import AsyncTeleBot
import json

settings_file = open("settings.json")
settings_json = json.load(settings_file)
bot = AsyncTeleBot(settings_json["token"])

@bot.message_handler(content_types=["new_chat_members"])
async def welcome_message(message):
    await bot.reply_to(message, "Hello!!! Welcome to the chat!!!")

@bot.message_handler(content_types=["left_chat_member"])
async def left_message(message):
    await bot.reply_to(message, "Oh, no!!! Come back!!!")

import asyncio
asyncio.run(bot.polling())