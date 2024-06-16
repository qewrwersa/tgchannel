from aiogram_dialog.widgets.kbd import Start
from aiogram_dialog.widgets.text import Const
from . import states

MAIN_MENU_BUTTON = Start(
    text=Const("Главное меню"),
    id="__main__",
    state=states.Main.MAIN,
)