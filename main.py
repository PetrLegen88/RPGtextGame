from Charakters import *
from enviroment import critical

import random


def fight(hero, monster):
    while hero.hp >= 0 and monster.hp >= 0:
        critical(hero, monster)
    if monster.hp <= 0:
        print(f"Hero {hero.name} have killed Monster, what will be your next move?")
    else:
        print("Game over")


fight(hero, monster1)
