from editor.question import Question
from editor.shared.resolve_room_attachment import resolve_room_attachment


ROOM_QUESTIONS: list[Question] = [
    Question("room_name", "Room name"),
    Question("room_description", "Room description"),
    Question("things_in_room", "What's in the room"),
    Question("attached", "How is the room attached", resolve_room_attachment),
]
