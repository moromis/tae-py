from editor.edit.item import edit_item
from editor.edit.room import edit_room
from editor.new.item import new_item
from editor.new.room import new_room
from editor.save import save_game


COMMANDS = {
    "new": {"room": new_room, "item": new_item},
    "edit": {"room": edit_room, "item": edit_item},
    "save": save_game,
}
