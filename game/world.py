import typing
from typing import Optional

if typing.TYPE_CHECKING:
    from game.characters import Character


class Room:

    def __init__(self) -> None:
        self._characters = []

    def add_character(self, character):
        self._characters.append(character)

    def get_characters(self):
        for ch in self._characters:
            yield ch

    def get_character_by_name(self, name: str) -> Optional['Character']:
        for ch in self._characters:
            if ch.name == name:
                return ch
        # TODO: handle if character not there
