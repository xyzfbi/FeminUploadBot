from aiogram.fsm.state import State, StatesGroup


class WaitingLinkState(StatesGroup):
    waiting_for_link = State()
