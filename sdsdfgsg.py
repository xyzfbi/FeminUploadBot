import asyncio
from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from yandex_music import Client
import services.yandex_music.yandex_sync as ym
from config.get_env import YANDEX_TOKEN

# Определяем состояния
class WaitingLinkState(StatesGroup):
    waiting_for_link = State()  # Состояние ожидания ссылки

router = Router()

@router.message(Command('yandex'))
async def start_yandex(message: Message, state: FSMContext):
    await state.set_state(WaitingLinkState.waiting_for_link)
    await message.reply("ватафак нигга грузи ссылочку на яндекс тречок")

@router.message(WaitingLinkState.waiting_for_link)
async def process_yandex_link(message: Message, state: FSMContext):
    link = message.text
    loading_message = await message.reply("Загрузка пошла")
    try:
        ya_client = Client(YANDEX_TOKEN).init()
        id_track = ym.extract_id_from_url(link)
        track_id, cover_id = await save_track_yandex_async(ya_client, id_track)
        if track_id and cover_id:
            await loading_message.edit_text(f"Трек сохранен под id = {track_id} и его обложка под id = {cover_id}")
        else:
            await loading_message.edit_text("Трек не сохранен ((")
    except Exception as e:
        await loading_message.edit_text(f"Произошла ошибка: {str(e)}")
    await state.clear()

async def save_track_yandex_async(ya_client: Client, track_id: int):
    return await asyncio.to_thread(ym.save_track, ya_client, track_id)
