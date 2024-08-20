from editor.main import editor_main
from editor.strings import strings
from shared import cls, output, read


def main():
    cls()
    editor_main()
    output(strings["STARTUP"])
    output(strings["SELECT_EDITOR_OR_PLAYER"])
    selection = read()
    if selection == "1":
        cls()
        editor_main()
    else:
        cls()
        main()


if __name__ == "__main__":
    main()
