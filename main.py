import os
import sys

from aiogram import types

from config import *
from tg_bot.handlers import bot, dp, start


from fastapi import FastAPI, Request

app = FastAPI()


@app.route(f'/{BOT_API_TOKEN}', methods=['POST'])
async def redirect_message(request: Request):
    json_string = request.get().json().decode('utf-8')
    update = types.Update.as_json(json_string)
    await dp.process_updates([update])


if __name__ == '__main__':
    bot.delete_webhook()
    bot.set_webhook(APP_URL)
    os.system('uvicorn main:app --reload')
