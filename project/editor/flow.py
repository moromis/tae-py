from editor.question import Question
from shared.read import read


def flow(questions: list[Question], prev_obj=None):
    final_obj = prev_obj if prev_obj else {}
    for q in questions:
        query, key = q
        answer = read(query)
