from aiogram.types import User
from aiogram_dialog import (
    Dialog, Window, LaunchMode,
)
from aiogram_dialog.widgets.text import Const

from src.common.config.bot import BotConfig
from src.infra.database.dao.holder import HolderDAO
from . import states

admins = BotConfig.compose().admins


async def get_user_data(dao: HolderDAO, event_from_user: User, **kwargs):
    user = await dao.user.get_user(event_from_user.id)
    if not user:
        user = await dao.user.add_user(event_from_user.id, "@" + event_from_user.username)
        await dao.commit()

    return {"user_id": user.id}


main_dialog = Dialog(
    Window(
        Const("Добро пожаловать.\n"),
        state=states.Main.MAIN,
        getter=get_user_data
    ),
    launch_mode=LaunchMode.ROOT
)
