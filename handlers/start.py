from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    # await message.reply("hi")
    await message.answer(f"hi {message.from_user.username} {message.from_user.first_name}")

