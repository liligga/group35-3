from aiogram import Router, types
from aiogram.filters import Command


picture_router = Router()

@picture_router.message(Command("pic"))
async def pic(message: types.Message):
    file = types.FSInputFile("images/cat.jfif")
    await message.answer_photo(
        photo=file,
        caption="Кошка"
    )
