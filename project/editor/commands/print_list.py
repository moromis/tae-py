from editor.commands.commands import COMMANDS
from editor.strings import strings
from shared.output import output


def print_list(root: str = "") -> str:
    output(strings["OPTIONS"])
    if not root or root == "":
        output("- " + "\n- ".join(COMMANDS.keys()))
