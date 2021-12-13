import logging
import ssl
from aiohttp import web


from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import get_new_configured_app
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook

from config import BOT_API_TOKEN

API_TOKEN = BOT_API_TOKEN

WEBHOOK_HOST = "https://test-bot-twitter.herokuapp.com/"
WEBHOOK_PATH = "/run.py"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '54.228.42.199'
WEBAPP_PORT = 443

logging.basicConfig(level=logging.INFO)

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def startcom(message: types.Message):
    await message.reply('Hi, user!')


async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)

    webhook = await bot.get_webhook_info()
    if webhook.url != WEBHOOK_URL:
        if not webhook.url:
            await bot.delete_webhook()

        await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown():
    logging.warning('Shutting down..')
    await bot.delete_webhook()


if __name__ == "__main__":

    app = get_new_configured_app(dispatcher=dp, path=WEBHOOK_PATH)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)

    web.run_app(app, host=WEBAPP_HOST, port=WEBAPP_PORT)