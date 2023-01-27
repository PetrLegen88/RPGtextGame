from game.characters import Player, Monster
from game.interaction import critical


monster1 = Monster(10, 100, 5, 5)
hero = Player("Amazon", 100, damage=10, defence=1)


def fight(hero, monster):
    while hero.hp > 0 and monster.hp > 0:
        critical(hero, monster)
    if monster.hp <= 0:
        print(f"Hero {hero.name} have killed Monster, what will be your next move?")
    else:
        print("Game over")


fight(hero, monster1)
