from project.editor.edit.item import edit_item
from project.editor.edit.room import edit_room
from project.editor.new.item import new_item
from project.editor.new.room import new_room
from project.editor.save import save_game


COMMANDS = {
    "new": {"room": new_room, "item": new_item},
    "edit": {"room": edit_room, "item": edit_item},
    "save": save_game,
}
