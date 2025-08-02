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

router = Router()

@router.message(Command('yandex'))
async def start_yandex(message: Message, state: FSMContext):
    await state.set_state(s.WaitingLinkState.waiting_for_link)
    await message.reply("ватафак нигга грузи ссылочку на яндекс тречок")


@router.message(State(s.WaitingLinkState.waiting_for_link))
async def process_yandex_link(message: Message, state: FSMContext):

    link = message.text
    import logging
    logger = logging.getLogger(__name__)

    # В обработчике:
    logger.info(f"Received link: {link}")
    loading_message = await message.reply("Загрузка пошла")
    try:
        ya_Client = Client(YANDEX_TOKEN).init()
        id_track = ym.extract_id_from_url(link)

        track_id, cover_id = await save_track_yandex_async(ya_Client, id_track)
        if track_id and cover_id:
            await loading_message.edit(f"Трек сохранен под id = {track_id} и его обложка под id = {cover_id}")
        else:
            await loading_message.edit("Трек не сохранен ((")
    except Exception as e:
        await loading_message.edit(f"Произолшла ошибка {str(e)}")

    await state.clear()


async def save_track_yandex_async(ya_client: Client, track_id: int):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, ym.save_track, ya_client, track_id)