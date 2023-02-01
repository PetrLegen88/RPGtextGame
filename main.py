from game.characters import Player, Monster
from game.interaction import fight

monster1 = Monster(10, 100, 5, 5)
hero = Player("Amazon", 100, damage=10, defence=1)

fight(hero, monster1)
