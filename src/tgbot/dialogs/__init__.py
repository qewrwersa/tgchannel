from aiogram import Router, Dispatcher

from src.tgbot.dialogs.main import main_dialog


def register_dialogs(dp: Dispatcher):
    dialog_router = Router()
    dialog_router.include_routers(
        main_dialog,
    )
    dp.include_router(dialog_router)
