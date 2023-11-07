import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import logging


BOT_TOKEN = '6553398272:AAHZU4mzCRhFC8ucPLLZH7cGHfdolDiHCWQ'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    # await message.reply("hi")
    await message.answer(f"hi {message.from_user.username} {message.from_user.first_name}")

@dp.message(Command("pic"))
async def pic(message: types.Message):
    file = types.FSInputFile("images/cat.jfif")
    await message.answer_photo(
        photo=file,
        caption="Кошка"
    )

@dp.message()
async def echo(message: types.Message):
    # print(message)
    # print(message.text)
    # await message.answer("hi")
    await message.answer(message.text)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())