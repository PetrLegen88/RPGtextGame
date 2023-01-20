from Charakters import Player, Monster
import random


def critical(self):
    if random.randint(1, 8) == 1:
        self.Monster.HP -= ((self.Player.damage * 2) - self.Monster.defence)
        print(f"Monster HP: {self.Monster.HP}")
        self.Player.HP -= (self.Monster.damage - self.Player.defence)
        print(f"Player HP: {self.Player.HP}")
    else:
        self.Monster.HP -= (self.Player.damage - self.Monster.defence)
        print(f"Monster HP: {self.Monster.HP}")
        self.Player.HP -= (self.Monster.damage - self.Player.defence)
        print(f"Player HP: {self.Player.HP}")


def fight(self):
    while self.Player.HP >= 0 and self.Monster.HP >= 0:
        critical(self)
    if self.Monster.HP <= 0:
        print("You have killed Monster, what will be your next move?")
    else:
        print("Game over")


fight()
