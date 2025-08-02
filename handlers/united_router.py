from aiogram import Router
from handlers.routers.feedback import router as feedback_router
from handlers.routers.help import router as help_router
from handlers.routers.start import router as start_router
from handlers.routers.yandex import router as yandex_router

router = Router()

router.include_router(feedback_router)
router.include_router(help_router)
router.include_router(start_router)
router.include_router(yandex_router)
