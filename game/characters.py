class Character:
    Character = []

    def __init__(self, hp: int, damage: int, defence: int, room=None):
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.room = room


class Player(Character):
    Player = []

    def __init__(self, name: str, hp: int, damage: int, defence: int, room=None):
        super().__init__(hp, damage, defence, room)
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.room = room


class Monster(Character):
    Monster = []

    def __init__(self, hp: int, damage: int, defence: int, room=None):
        super().__init__(hp, damage, defence, room)
        self.hp = hp
        self.damage = damage
        self.defence = defence
        self.room = room
