from aiogram import Dispatcher, Bot, executor, types
from config import BOT_API_TOKEN, APP_URL

bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    username = message.from_user.username
    await message.reply(f'Hi, {username}!')
