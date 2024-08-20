from dataclasses import dataclass, astuple


@dataclass
class Question:
    key: str
    query: str
