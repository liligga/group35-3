from aiogram import Router, F,types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


questions_router = Router()


class Questionaire(StatesGroup):
    name = State()
    age = State()
    gender = State()
    country = State()


# FSM - Finite state machine(Конечный автомат)
@questions_router.message(Command("quest"))
async def start_questions(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.name)
    await message.answer("Как Вас зовут?")


@questions_router.message(F.text, Questionaire.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(Questionaire.age)
    await message.answer("Какой у Вас возраст?")


@questions_router.message(F.text, Questionaire.age)
async def process_age(message: types.Message, state: FSMContext):
    # check age
    await message.answer("Спасибо")
