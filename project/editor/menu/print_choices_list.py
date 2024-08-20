from editor.menu.choices import CHOICES
from editor.strings import strings
from shared import get_from_path
from shared.output import output


def _print_choices(choices):
    output("- " + "\n- ".join([x.title() for x in choices.keys()]))


def print_choices_list(root: str = "") -> str:
    output(strings["OPTIONS"])
    if not root or root == "":
        _print_choices(CHOICES)
    else:
        choices = get_from_path(root, CHOICES)
        _print_choices(choices)
