from aiogram import Router, F, types
from aiogram.filters import Command
from pprint import pprint


group_messages_router = Router()
BAD_WORDS = ("дурак", "плохой")


@group_messages_router.message(F.chat.type == "group")
@group_messages_router.message(Command("ban", prefix="!/"))
async def ban_user(message: types.Message):
    reply = message.reply_to_message
    if reply is not None:
        await message.bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=reply.from_user.id
        )


@group_messages_router.message(F.chat.type == "group")
async def catch_bad_words(message: types.Message):
    # print(message.chat.type)
    for word in BAD_WORDS:
        # "дурак" == "Дурак"
        if word in message.text.lower():
            await message.reply(f"Нельзя использовать слово {word}!")
            await message.delete()
            break


