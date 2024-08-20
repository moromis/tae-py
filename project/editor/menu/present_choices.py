from editor import strings
from editor.menu.handle_menu_choice import handle_menu_choice
from editor.menu.print_choices_list import print_choices_list
from shared import cls
from shared.output import output
from shared.read import read


def present_choices(path: str = "") -> str:
    print_choices_list(path)
    output("\n")
    choice = read(strings["WHAT_TO_DO"])
    new_path = path + "." + choice if path != "" else choice
    result = handle_menu_choice(new_path)
    if not result:
        cls()
        present_choices(choice)
    return new_path
