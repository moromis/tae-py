from editor.question import Question
from shared.output import output
from shared.read import read
from string import capwords


def flow(questions: list[Question], prev_obj=None):
    final_obj = prev_obj if prev_obj else {}
    for q in questions:
        answer = None
        query = capwords(q.query.strip("?")) + "?"
        if not q.func:
            answer = read(query)
        else:
            output(query)
            answer = q.func()
        final_obj[q.key] = answer
    return final_obj
