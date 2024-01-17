from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


menu_start = ReplyKeyboardMarkup(
    keyboard= [
       [
           KeyboardButton(text="Animeni ko'rish 👀"),
       ],
       [
           KeyboardButton(text="Anime kanali"),
       ],
    ],
    resize_keyboard=True
)

Anime_bot = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="1-2 Qismlar ✔️"),
            KeyboardButton(text="3-4 Qismlar ✔️"),
            KeyboardButton(text="5-6 Qismlar ✔️")
        ],
        [
            KeyboardButton(text="7-8 Qismlar ✔️"),
            KeyboardButton(text="9-10 Qismlar ✔️"),
            KeyboardButton(text="11-12 Qismlar ✔️")
        ],
         [
            KeyboardButton(text="13-14 Qismlar ✔️"),
            KeyboardButton(text="15-16 Qismlar ✔️"),
            KeyboardButton(text="17-18 Qismlar ✔️")
        ],
          [
            KeyboardButton(text="19-20 Qismlar ✔️"),
            KeyboardButton(text="21-22 Qismlar ✔️"),
            KeyboardButton(text="23 Qism (final) ✔️")
        ],
    ]
)