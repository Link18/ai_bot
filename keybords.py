from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

start_menu=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='создать картинку'),KeyboardButton(text='чат бот')],
    [KeyboardButton(text='личный кабинет')]
])

chat_menu=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='OpenAI',callback_data='openai'),
     InlineKeyboardButton(text='Mistral_AI',callback_data='mistral')]
    ])

stop_button=ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='стоп')]
])

mistral_keybord=InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='chat bot',callback_data='chat-bot')]])