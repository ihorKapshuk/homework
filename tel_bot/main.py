from decouple import config
from other_functions import checker
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

def build_keyboard():
    keyboard = [
        [InlineKeyboardButton("Одеса", callback_data="1")],
        [InlineKeyboardButton("Київ", callback_data="2")],
        [InlineKeyboardButton("Львів", callback_data="3")],
        [InlineKeyboardButton("Аненталь", callback_data="4")],
        [InlineKeyboardButton("Миколаїв", callback_data="5")],
        [InlineKeyboardButton("Херсон", callback_data="6")],
        [InlineKeyboardButton("Запоріжжя", callback_data="7")],
        [InlineKeyboardButton("Донецьк", callback_data="8")],
        [InlineKeyboardButton("Луганськ", callback_data="9")],
        [InlineKeyboardButton("Харків", callback_data="10")],
        [InlineKeyboardButton("Дніпро", callback_data="11")],
        [InlineKeyboardButton("Кропивницький", callback_data="12")],
        [InlineKeyboardButton("Вінниця", callback_data="13")],
        [InlineKeyboardButton("Тернопіль", callback_data="14")],
        [InlineKeyboardButton("Чернівці", callback_data="15")],
        [InlineKeyboardButton("Івано-Франківськ", callback_data="16")],
        [InlineKeyboardButton("Ужгород", callback_data="17")],
        [InlineKeyboardButton("Луцьк", callback_data="18")],
        [InlineKeyboardButton("Рівне", callback_data="19")],
        [InlineKeyboardButton("Житомир", callback_data="20")],
        [InlineKeyboardButton("Чернігів", callback_data="21")],
        [InlineKeyboardButton("Суми", callback_data="22")],
        [InlineKeyboardButton("Полтава", callback_data="23")],
        [InlineKeyboardButton("Черкаси", callback_data="24")],
        [InlineKeyboardButton("Сімферополь", callback_data="25")],  
        [InlineKeyboardButton("Севастополь", callback_data="26")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Says hello"""
    await update.message.reply_text("Привіт! Цей бот показує погоду.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Напишіть /weather для того щоб подивитись погоду.")

async def show_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with buttons named cities."""
    await update.message.reply_text("Прогноз погоди на наступну годину:", reply_markup=build_keyboard())


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()
    await query.edit_message_text(text=checker(query.data), reply_markup=build_keyboard())


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(config("SECRET_TOKEN")).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("weather", show_command))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()