from project.parser.sanitize import sanitize
from project.parser.split_by_and import split_by_and


def _parse(command: str) -> str:
    # get indirect object, direct object, verb
    split_command = command.split(" ")
    verb = get_verb(split_command)

    pass


def parse(command: str) -> str:
    sanitized = sanitize(command)
    commands = split_by_and(sanitized)
    for c in commands:
        _parse(c)
