from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.utils import executor

api = '7753786587:AAH09YzoR41hz9b1MsamAex9Gc2HcbG21rc'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.")


@dp.message_handler()
async def all_message(message):
    if message.text == '/start':
        return
    else:
        await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
