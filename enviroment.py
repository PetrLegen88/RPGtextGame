import random


def critical(hero, monster):
    if random.randint(1, 8) == 1:
        monster.hp -= ((hero.damage * 2) - monster.defence)
        print(f"Monster HP: {monster.hp}")
        hero.hp -= (monster.damage - hero.defence)
        print(f"Player HP: {hero.hp}")
    else:
        monster.hp -= (hero.damage - monster.defence)
        print(f"Monster HP: {monster.hp}")
        hero.hp -= (monster.damage - hero.defence)
        print(f"Player HP: {hero.hp}")
