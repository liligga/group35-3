from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

questions_router = Router()


class Questionaire(StatesGroup):
    name = State()
    age = State()
    gender = State()
    country = State()


# FSM - Finite state machine(Конечный автомат)
@questions_router.message(Command("stop"))
@questions_router.message(F.text=="stop")
async def stop_questions(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Вопросы прерваны")


@questions_router.message(Command("quest"))
async def start_questions(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.name)
    await message.answer("Для выхода введите 'stop'")
    await message.answer("Как Вас зовут?")


@questions_router.message(F.text, Questionaire.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)

    await state.set_state(Questionaire.age)
    await message.answer("Какой у Вас возраст?")


@questions_router.message(F.text, Questionaire.age)
async def process_age(message: types.Message, state: FSMContext):
    # check age
    age = message.text.strip()
    if not age.isdigit():
        await message.answer("Возраст должен быть числом")
    elif int(age) < 12 or int(age) > 100:
        await message.answer("Возраст должен быть от 12 до 100")
    else:
        await state.update_data(age=int(age))

        kb = types.ReplyKeyboardMarkup(
            keyboard=[
                [
                    types.KeyboardButton(text="Мужской"),
                    types.KeyboardButton(text="Женский")
                ]
            ]
        )
        await state.set_state(Questionaire.gender)
        await message.answer("Ваш пол?")


@questions_router.message(F.text, Questionaire.gender)
async def process_gender(message: types.Message, state: FSMContext):
    await state.update_data(gender=message.text)

    # save to DB
    data = await state.get_data()
    print(data)
    # clear state and Bye message
    await state.clear()
    await message.answer("Спасибо, мы с вами свяжемся")




