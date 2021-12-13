import logging
import ssl
from aiohttp import web


from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import get_new_configured_app
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

from config import BOT_API_TOKEN, APP_URL

API_TOKEN = BOT_API_TOKEN

WEBHOOK_HOST = "https://test-bot-twitter.herokuapp.com/"
WEBHOOK_PATH = "/run.py"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '54.78.134.111'
WEBAPP_PORT = 443

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def startcom(message: types.Message):
    await message.reply('Hi, user!')


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

    webhook = await bot.get_webhook_info()
    if webhook.url != WEBHOOK_URL:
        if not webhook.url:
            await bot.delete_webhook()

        await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()


if __name__ == "__main__":

    await bot.delete_webhook()
    await bot.set_webhook(APP_URL)

    # start_webhook(
    #     dispatcher=dp,
    #     webhook_path=WEBHOOK_PATH,
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    #     host=WEBAPP_HOST,
    #     port=WEBAPP_PORT
    # )