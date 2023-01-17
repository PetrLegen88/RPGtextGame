import random


def fight():
    while Monster.HP >= 0 and Player.HP >= 0:               # I dont know why it works with "and" condition instead "or"
        Monster.HP -= (Player.damage - Monster.defence)
        print(f"Monster HP: {Monster.HP}")                  # Debug print
        Player.HP -= (Monster.damage - Player.defence)
        print(f"Player HP: {Player.HP}")                    # Debug print
    if Monster.HP <= 0:
        print("You have killed Monster, what will be your next move?")
    else:
        print("Game over")


class Player:
    damage = 7
    HP = 1000
    defence = 3


class Monster:
    damage = 5
    HP = 100
    defence = 1


fight()
