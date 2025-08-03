import asyncio
from config.get_env import TELEGRAM_TOKEN
from aiogram import Dispatcher, Bot
from handlers.united_router import router as united_router
from database.supabase_connection import get_supabase
bot = Bot(TELEGRAM_TOKEN)
dp = Dispatcher()

dp.include_router(united_router)

async def main():
    supabase_client = get_supabase()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())