from aiogram import Router, F ,types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start(message: types.Message):
    # await message.reply("hi")
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(
                    text="Наш сайт", url="https://google.com"
                ),
                types.InlineKeyboardButton(
                    text="Наш инстаграм", url="https://instagram.com"
                )
            ],
            [
                types.InlineKeyboardButton(
                    text="О нас", callback_data="about"
                )
            ]
        ]
    )
    
    await message.answer(
        f"Привет, @{message.from_user.username} тебя зовут:{message.from_user.first_name}",
        reply_markup=kb
    )


@start_router.callback_query(F.data == "about")
async def about_us(callback: types.CallbackQuery):
    await callback.answer() # чтобы долго не грузилось
    await callback.message.answer("Текст 'О нас'")