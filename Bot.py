from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from Scraper import scrape_server
import os

bot = Bot(token="BOT_TOKEN")

dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'info'])
async def welcome(message: types.Message):
    await message.answer("This bot provides you with scraped V2Ray Servers.\n/info - Information\n/request - Request new server list in csv format") #, reply_markup=kb1)

@dp.message_handler(commands=['request'])
async def request(message: types.Message):


    await message.answer_document(scrape_server())

executor.start_polling(dp)


