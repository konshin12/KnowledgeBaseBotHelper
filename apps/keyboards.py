from aiogram import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from config import buttons_dict
import emoji

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Работа с клиентами', callback_data='client')]
])


kb_abbr = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Полный список", callback_data="fullList")]
    ]
)

async def update():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Обновления', callback_data='updates'))
    return keyboard.adjust(1).as_markup()

async def hide():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Скрыть', callback_data='hide'))
    return keyboard.adjust(1).as_markup()

async def inline_softs():
    keyboard = InlineKeyboardBuilder()
    add_buttons(keyboard, buttons_dict)
    add_back_button(keyboard)
    return keyboard.adjust(2).as_markup()
async def inline_abbr():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="Полный список", callback_data="fullList"))
    add_back_button(keyboard)
    return keyboard.adjust(1).as_markup()
async def inline_proc():
    keyboard = InlineKeyboardBuilder()
    add_first_proc_button(keyboard)
    add_second_proc_button(keyboard)
    add_back_button(keyboard)
    return keyboard.adjust(1).as_markup()

async def inline_first_proc():
    keyboard = InlineKeyboardBuilder()
    add_second_proc_button(keyboard)
    add_back_button(keyboard)
    return keyboard.adjust(1).as_markup()

async def inline_second_proc():
    keyboard = InlineKeyboardBuilder()
    add_first_proc_button(keyboard)
    add_back_button(keyboard)
    return keyboard.adjust(1).as_markup()

def add_back_button(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text="Назад", callback_data="back"))
def add_back2_button(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text="На главную", callback_data="back2"))

def add_second_proc_button(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text="Часть вторая", callback_data="secondproc"))
def add_first_proc_button(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text="Часть первая", callback_data="firstproc"))

async def inline_client():
    keyboard = InlineKeyboardBuilder()
    add_pattern_button(keyboard)
    keyboard.add(InlineKeyboardButton(text='Софтик', callback_data='soft')),
    keyboard.add(InlineKeyboardButton(text='Аббревиатуры', callback_data='abbr'))
    keyboard.add(InlineKeyboardButton(text='Процедуры', callback_data='proc')),
    keyboard.add(InlineKeyboardButton(text='Полезные ссылки', callback_data='usefullurl'))
    add_back2_button(keyboard)
    return keyboard.adjust(1).as_markup()

async def inline_client2():
    keyboard = InlineKeyboardBuilder()
    add_pattern_button(keyboard)
    keyboard.add(InlineKeyboardButton(text='Софтик', callback_data='soft')),
    keyboard.add(InlineKeyboardButton(text='Аббревиатуры', callback_data='abbr'))
    keyboard.add(InlineKeyboardButton(text='Процедуры', callback_data='proc')),
    keyboard.add(InlineKeyboardButton(text='Полезные ссылки', callback_data='usefullurl'))
    add_back_button(keyboard)
    return keyboard.adjust(1).as_markup()
def add_buttons(keyboard: InlineKeyboardBuilder, buttons_dict: dict):
    for button_text, callback_data in buttons_dict.items():
        keyboard.row(InlineKeyboardButton(text=button_text, callback_data=callback_data))

def add_pattern_button(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text='Полезные шаблоны', callback_data='pattern'))

async def inline_patterns():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Pro', callback_data='tinkoffpro'))
    keyboard.add(InlineKeyboardButton(text='Программы лояльности', callback_data='creditcardpromotion'))
    keyboard.add(InlineKeyboardButton(text='Переводы', callback_data='transfers'))
    keyboard.add(InlineKeyboardButton(text='Лимиты', callback_data='limits'))
    keyboard.add(InlineKeyboardButton(text='Снятие комиссия', callback_data='withdrawl'))
    keyboard.add(InlineKeyboardButton(text='Пополнение комиссия', callback_data='replenishment'))
    keyboard.add(InlineKeyboardButton(text='Обслуживание', callback_data='cardservice'))
    add_back_button(keyboard)
    return keyboard.adjust(2).as_markup()

async def inline_back():
    keyboard = InlineKeyboardBuilder()
    add_back3_button(keyboard)
    return keyboard.adjust(1).as_markup()

def add_back3_button(keyboard: InlineKeyboardBuilder):
    keyboard.row(InlineKeyboardButton(text="К шаблонам", callback_data="back3"))