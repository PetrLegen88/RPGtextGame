from game.characters import Player, Monster
from game.interaction import fight
from game.world import Room

room1 = Room()

monster1 = Monster(10, 100, 5, room1)
hero = Player("Amazon", 100, damage=10, defence=1, room=room1)

monster1.name
hero.name

hero.observe()

for i in range(10):
    Monster(10, 100, 5, room1)

hero.observe()

hero.attack("Monster9")

hero.hp = 1000

fight(hero, monster1)



