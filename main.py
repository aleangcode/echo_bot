# импортируем нужные библиотеки
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# токен из BotFather
API_TOKEN = '6502002195:AAHQBAM9tyafOZl4hnjphoEAf4Sr9PvRWWU'

# инициализируем нового бота
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Я эхо-бот. Отправь мне сообщение, и я повторю его.")


# реакция бота на текст
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def echo_message(message: types.Message):
    await message.answer(message.text)

# запускаем бота
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True)

# pip install aiogram
