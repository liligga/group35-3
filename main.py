import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging
from dotenv import load_dotenv
from os import getenv
from handlers import start_router


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()

@dp.message(Command("pic"))
async def pic(message: types.Message):
    file = types.FSInputFile("images/cat.jfif")
    await message.answer_photo(
        photo=file,
        caption="Кошка"
    )

# @dp.message()
async def echo(message: types.Message):
    # print(message)
    # print(message.text)
    # await message.answer("hi")
    await message.answer(message.text)

async def main():
    dp.include_router(start_router)


    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())