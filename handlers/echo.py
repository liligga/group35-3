from aiogram import Router, types

echo_router = Router()

@echo_router.message()
async def echo(message: types.Message):
    # print(message)
    # print(message.text)
    # await message.answer("hi")
    await message.answer(message.text)