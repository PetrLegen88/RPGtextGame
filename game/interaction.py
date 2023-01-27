"""
Tento modul obsahuje funkce pro interakci různých herních entit = hráči a monsttra, například...
"""


# TODO: add hints


def provoke(attacker: 'Player', defender:'Monster'):
    """
    Player může provokovat příšeru, což ji rozlítí a zvedne ji to attack, ale taky ji to sníží defence level,
    hráči to taky přídá defense level
    """

    print("Hey monster! I will punish you!")
    print("Measly human, I will kill you!")

    defender.damage += 1
    defender.defence -= 2

    attacker.defence += 1



