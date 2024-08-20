from editor.flow import flow
from editor.questions.room import ROOM_QUESTIONS


def new_room():
    print("make a new room")
    room = flow(ROOM_QUESTIONS)
    print("saving room:\n", room)
