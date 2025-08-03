import asyncio

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import Message
from yandex_music import Client
import services.yandex_music.yandex_sync as ym
import schemas.state_schemas as s
from config.get_env import YANDEX_TOKEN
from database.supabase_connection import get_supabase
router = Router()

@router.message(Command('yandex'))
async def start_yandex(message: Message, state: FSMContext):
    await state.set_state(s.WaitingLinkState.waiting_for_link)
    await message.reply("ватафак нигга грузи ссылочку на яндекс тречок")


@router.message(s.WaitingLinkState.waiting_for_link)
async def process_yandex_link(message: Message, state: FSMContext):
    await state.update_data(waiting_link=message.text)
    link = message.text
    import logging
    logger = logging.getLogger(__name__)

    # В обработчике:
    logger.info(f"Received link: {link}")
    loading_message = await message.reply("аплоад на ск пошел")
    try:
        ya_Client = Client(YANDEX_TOKEN).init()
        supabase: Client = get_supabase()
        id_track = ym.extract_id_from_url(link)

        track_id, cover_id = await save_track_yandex_async(ya_Client, id_track)
        if track_id and cover_id:
            await loading_message.edit_text(f"БРАТУХ ТВОЙ СВАГОВЫЙ ТРЕЧОК СОХРАНЕН ЕПТА")
        else:
            await loading_message.edit_text("эх бля трек не сохранен ((")
    except Exception as e:
        await loading_message.edit_text(f"сука ошибка {str(e)}")

    await state.clear()


async def save_track_yandex_async(ya_client: Client, track_id: int):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, ym.save_track, ya_client, track_id)