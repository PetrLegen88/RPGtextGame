import typing

from .interaction import fight

if typing.TYPE_CHECKING:
    from .world import Room


class Character:

    def __init__(self, hp: int, damage: int, defence: int, room):
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.add_to_room(room)

    def add_to_room(self, room: 'Room'):
        self.room = room
        self.room.add_character(self)


class Player(Character):
    Player = []

    def __init__(self, name: str, hp: int, damage: int, defence: int, room):
        super().__init__(hp, damage, defence, room)
        self.name = name

    def observe(self):
        for character in self.room.get_characters():
            print(f"There is {character.name} in the same room")

    def attack(self, target: str):
        target_object = self.room.get_character_by_name(target)
        if target_object is None:
            print("There is no such a monster")
            return

        fight(self, target_object)




class Monster(Character):
    monsters = []

    def __init__(self, hp: int, damage: int, defence: int, room):
        super().__init__(hp, damage, defence, room)

        self.monsters.append(self)

        self.name = f"Monster{len(self.monsters)}"
