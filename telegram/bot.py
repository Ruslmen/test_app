import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

# Логи для отладки
logging.basicConfig(level=logging.INFO)

TOKEN = "8553570298:AAF8KiXFB1ue7yDl701LGc6ko3Y4sdDVzvE"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я твой новый тестовый бот.\n\n"
        "Что я умею пока:\n"
        "• /start — это сообщение\n"
        "• /help  — помощь\n"
        "• /test  — проверка работоспособности\n"
        "• любое другое сообщение — повторю его тебе"
    )

# Команда /help
@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Пока я очень простой бот.\n"
        "Напиши мне что угодно — я отвечу.\n\n"
        "Доступные команды:\n"
        "/start — начать общение\n"
        "/help — это сообщение\n"
        "/test — проверка"
    )

# Команда /test
@dp.message(Command("test"))
async def cmd_test(message: Message):
    await message.answer("✅ Бот работает!\nТвой ID: " + str(message.from_user.id))

# Ответ на любое текстовое сообщение (эхо)
@dp.message()
async def echo_handler(message: Message):
    if message.text:
        await message.answer(f"Ты написал:\n{message.text}")
    else:
        await message.answer("Я пока понимаю только текст 😅")

# Запуск бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())