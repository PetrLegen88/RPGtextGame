from game.interaction import provoke

from Charakters import Player, Monster


monster1 = Monster(10, 100, 5, 5)
player = Player("John", 100, damage=10, defence=10)

print(f"Stats - beginning {player.damage=}, {player.defence=}")
print(f"Stats - beginning {monster1.damage=}, {monster1.defence=}")

provoke(player, monster1)


print(f"Stats - end {player.damage=}, {player.defence=}")
print(f"Stats - end {monster1.damage=}, {monster1.defence=}")
