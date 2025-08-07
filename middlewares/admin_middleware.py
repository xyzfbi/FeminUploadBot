from aiogram import types
from aiogram.dispatcher.event.bases import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

ADMIN_IDS = [123456789, 987654321] # Example admin user IDs

class AdminAccessMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        if message.from_user.id not in ADMIN_IDS:
            await message.reply("You are not authorized to use this command.")
            raise CancelHandler() # Stop processing the update

# Register the middleware with your Dispatcher
# dp.middlewares.setup(AdminAccessMiddleware())