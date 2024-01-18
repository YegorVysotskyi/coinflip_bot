import logging
import random
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import CallbackContext

from app.db import DatabaseManager

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

DATABASE_FILE = "../coinflip.db"
database_manager = DatabaseManager(DATABASE_FILE)


async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [[KeyboardButton("Бросить Монетку"), KeyboardButton("История")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Добро пожаловать! Выберите команду:", reply_markup=reply_markup
    )


async def flip_coin(update: Update, context: CallbackContext) -> None:
    result = "Орёл" if bool(random.getrandbits(1)) else "Решка"
    await update.message.reply_text(f"Результат подбрасывания монетки: {result}")
    await database_manager.save_result(result)


async def show_stats(update: Update, context: CallbackContext) -> None:
    history = await database_manager.get_history()

    if history:
        stats = "\n".join([f"{i + 1}. {result[0]}" for i, result in enumerate(history)])
        await update.message.reply_text(f"Статистика предыдущих бросков:\n{stats}")
    else:
        await update.message.reply_text("Статистика предыдущих бросков отсутствует.")

