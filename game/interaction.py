"""
Tento modul obsahuje funkce pro interakci různých herních entit = hráči a monsttra, například...
"""
import typing

import random

if typing.TYPE_CHECKING:
    from .characters import Player, Monster


def provoke(attacker: 'Player', defender: 'Monster'):
    """
    Player může provokovat příšeru, což ji rozlítí a zvedne ji to attack, ale taky ji to sníží defence level,
    hráči to taky přídá defense level
    """

    print("Hey monster! I will punish you!")
    print("Measly human, I will kill you!")

    defender.damage += 1
    defender.defence -= 2

    attacker.defence += 1


def critical(hero: 'Player', monster: 'Monster'):
    if random.randint(1, 8) == 1:
        monster.hp -= ((hero.damage * 2) - monster.defence)
        print(f"Monster HP: {monster.hp}")
        hero.hp -= (monster.damage - hero.defence)
        print(f"Player {hero.name} HP: {hero.hp}")

    else:
        monster.hp -= (hero.damage - monster.defence)
        print(f"Monster HP: {monster.hp}")
        hero.hp -= (monster.damage - hero.defence)
        print(f"Player HP: {hero.hp}")


def fight(hero, monster):
    while hero.hp > 0 and monster.hp > 0:
        critical(hero, monster)
    if monster.hp <= 0:
        print(f"Hero {hero.name} have killed Monster, what will be your next move?")
    else:
        print("Game over")
