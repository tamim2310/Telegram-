import telebot
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from config import BOT_TOKEN, ADMIN_ID
from handlers import register_handlers

# Initialize bot with state storage
bot = telebot.TeleBot(BOT_TOKEN, state_storage=StateMemoryStorage())

# Define states for FSM
class UserState(StatesGroup):
    LANGUAGE = State()
    JOIN_VERIFICATION = State()
    BROKER_SELECTION = State()
    REGISTRATION = State()
    ACCOUNT_ID = State()
    QUOTE_TYPE = State()
    SIGNAL_TIME = State()
    CURRENCY_PAIR = State()
    SHOW_SIGNAL = State()

def main():
    # Register all handlers
    register_handlers(bot)
    
    # Start polling
    print("Bot is running...")
    bot.infinity_polling()

if __name__ == "__main__":
    main()
