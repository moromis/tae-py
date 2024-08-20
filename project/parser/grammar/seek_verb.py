from typing import Callable
from parser.grammar.verbs import STANDARD_VERBS


def seek_verb(verb: str) -> Callable:
    if verb in STANDARD_VERBS:
        return STANDARD_VERBS[verb]
    else:
        return None
