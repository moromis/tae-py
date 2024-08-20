from dataclasses import dataclass
from typing import Callable


@dataclass
class Question:
    key: str
    query: str
    func: Callable = None
