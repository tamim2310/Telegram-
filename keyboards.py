from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import YOUTUBE_LINK, TELEGRAM_LINK, POCKET_OPTION_LINK, QUOTEX_LINK, SUBSCRIBE_LINK

def language_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("বাংলা 🇧🇩", callback_data="lang_bn"))
    keyboard.add(InlineKeyboardButton("English 🇬🇧", callback_data="lang_en"))
    return keyboard

def join_channel_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("YouTube", url=YOUTUBE_LINK))
    keyboard.add(InlineKeyboardButton("Telegram", url=TELEGRAM_LINK))
    keyboard.add(InlineKeyboardButton("✅ Verify", callback_data="verify"))
    return keyboard

def broker_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Pocket Option", callback_data="broker_pocket"))
    keyboard.add(InlineKeyboardButton("Quotex", callback_data="broker_quotex"))
    return keyboard

def register_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("✅ Registered", callback_data="registered"))
    return keyboard

def quote_type_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Stock", callback_data="quote_stock"))
    keyboard.add(InlineKeyboardButton("OTC", callback_data="quote_otc"))
    keyboard.add(InlineKeyboardButton("⬅️ Back", callback_data="back_to_broker"))
    return keyboard

def signal_time_keyboard():
    keyboard = InlineKeyboardMarkup()
    times = ["5s", "30s", "1min", "3min", "5min", "10min", "15min", "30min"]
    for time in times:
        keyboard.add(InlineKeyboardButton(time, callback_data=f"time_{time}"))
    keyboard.add(InlineKeyboardButton("⬅️ Back", callback_data="back_to_quote"))
    return keyboard

def currency_pair_keyboard():
    keyboard = InlineKeyboardMarkup()
    pairs = ["CAD/JPY", "EUR/USD", "GBP/JPY", "AUD/CAD", "GBP/USD", "AUD/JPY", "EUR/GBP", "AUD/CHF"]
    for pair in pairs:
        keyboard.add(InlineKeyboardButton(pair, callback_data=f"pair_{pair}"))
    keyboard.add(InlineKeyboardButton("⬅️ Back", callback_data="back_to_time"))
    return keyboard

def signal_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔁 Next Signal", callback_data="next_signal"))
    keyboard.add(InlineKeyboardButton("⬅️ Back", callback_data="back_to_pair"))
    return keyboard

def subscribe_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("🔓 Subscribe", url=SUBSCRIBE_LINK, callback_data="subscribe"))
    return keyboard

def admin_verification_keyboard(user_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Approve", callback_data=f"approve_verify_{user_id}"))
    keyboard.add(InlineKeyboardButton("Reject", callback_data=f"reject_verify_{user_id}"))
    return keyboard

def admin_account_id_keyboard(user_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Approve", callback_data=f"approve_id_{user_id}"))
    keyboard.add(InlineKeyboardButton("Reject", callback_data=f"reject_id_{user_id}"))
    return keyboard

def admin_subscription_keyboard(user_id):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Approve", callback_data=f"approve_sub_{user_id}"))
    keyboard.add(InlineKeyboardButton("Reject", callback_data=f"reject_sub_{user_id}"))
    return keyboard
