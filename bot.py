from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from core import admin_start, add_queue
from cfg import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await admin_start(bot, message)


@dp.callback_query_handler(lambda c: c.data == "to_queue")
async def registration_handler(call: types.CallbackQuery):
    await add_queue(bot, call)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)