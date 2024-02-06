from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def queue_start_kb():
    add_queue = InlineKeyboardButton('Встать в очередь', callback_data= 'to_queue')
    chat_kb = InlineKeyboardMarkup().row(add_queue)
    return chat_kb
