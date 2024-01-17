from aiogram import Router,F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from loader import db
from keyboards.keyboards import  menu_start
from keyboards.keyboards import  Anime_bot
import sqlite3

menu_router: Router = Router()

@menu_router.message(F.text == "Anime kanali")
async def menu_button(message: Message):
    await message.answer("https://t.me/Anime_uzbekcha")
    
@menu_router.message(F.text == "Animeni ko'rish 👀")
async def menu_button(message: Message):
    await message.answer("Animeni ko'rish",reply_markup=Anime_bot)

@menu_router.message(F.text == "🔚 orqaga")
async def menu_button(message: Message ):
    await message.answer("🔚 Oraqaga",reply_markup=menu_start)