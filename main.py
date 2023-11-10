from aiogram.types import BotCommand
import asyncio
import logging
from bot import dp, bot
from handlers import (
    start_router, 
    echo_router,
    picture_router,
    shop_router
)


async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Начало"),
        BotCommand(command="pic", description="Показать картинку"),
        BotCommand(command="shop", description="Магазин"),
    ])

    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(shop_router)

    # в самом конце
    dp.include_router(echo_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())