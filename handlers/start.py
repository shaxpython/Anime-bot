from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from loader import db
from keyboards.keyboards import  menu_start
import sqlite3

start_router: Router = Router()

@start_router.message(Command('start'))
async def start_handler(message: Message):
    await message.answer(f"""Salom 😊  {message.from_user.full_name}
                         
Agarsiz 'odugarlar Jangi' nomli animeni ko;rmoqchi bo'lsangiz Adashmagansiz !""", reply_markup=menu_start)
    