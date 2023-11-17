import asyncio
import logging

from aiogram.types import BotCommand

from handlers.start import start
from bot import bot, dp
from handlers import (
    echo_router, picture_router, questions_router,
    shop_router, start_router)
from db.queries import init_db, create_tables, populate_tables


async def on_startup(dispatcher):
    init_db()
    create_tables()
    populate_tables()


async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Начало"),
        BotCommand(command="pic", description="Показать картинку"),
        BotCommand(command="shop", description="Магазин"),
        BotCommand(command="quest", description="Опросник"),
    ])

    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(shop_router)
    dp.include_router(questions_router)

    dp.startup.register(on_startup)
    # в самом конце
    dp.include_router(echo_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())