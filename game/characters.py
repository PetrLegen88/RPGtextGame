
class Player:

    def __init__(self, name: str, hp=100, damage=1, defence=1):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.defence = defence


class Monster:

    def __init__(self, level: int, hp: int, damage: int, defence: int):
        self.level = level
        self.hp = hp
        self.damage = damage
        self.defence = defence
