import asyncio
import logging
from aiogram import Bot, Dispatcher
import os
from dotenv import load_dotenv
from handlers import router

# Включаем логирование, чтобы не пропустить важные сообщения

# Объект бота
bot = Bot(token="7220974259:AAG7yXrOjFfITdJIElkmWImLBR7M9UgobSU")
# Диспетчер
dp = Dispatcher()



# Запуск процесса поллинга новых апдейтов
async def main():
    # load_dotenv()
    dp.include_router(router)
    await dp.start_polling(bot)
    
     



if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('ВЫКЛ')
