from aiogram.bot import Bot
from aiogram.utils import executor
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from config import token, words
from db_api import create_db, store_info
from datetime import datetime

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(content_types=["text"])
async def filter_text(message):
    if message.chat.type != "private":
        admins_list = [
            admin.user.id
            for admin in await bot.get_chat_administrators(chat_id=message.chat.id)
        ]
        if message.from_user.id not in admins_list:
            if any(word in message.text for word in words):
                store_info(
                    message.from_user.id,
                    message.from_user.first_name,
                    message.from_user.last_name,
                    message.from_user.username,
                    message.text,
                    datetime.now(),
                )


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=create_db())
