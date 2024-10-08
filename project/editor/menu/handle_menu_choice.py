from editor.menu.choices import CHOICES
from shared import get_from_path
from shared.cls import cls


def handle_menu_choice(path: str) -> None:
    # run given function based on passed path
    menu_choice_result = get_from_path(path, CHOICES)
    if callable(menu_choice_result):
        cls()
        menu_choice_result()
        return True
    else:
        return False
