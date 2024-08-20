from editor.strings import strings
from editor.commands.print_list import print_list
from shared.output import output
from shared.read import read


if __name__ == "__main__":
    output(strings["STARTUP"])
    output(print_list())
    read(strings["WHAT_TO_DO"])
