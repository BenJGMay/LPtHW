from sys import exit
from random import randint
from textwrap import dedent

player_inventory = []
player_hp = 12
player_damage = randint(0, 3)
player_attacks = [
"lunge forwards and strike a blow!",
"keep your guard up and counterattack!",
"target your opponent's genitals!",
"hurl literally painful insults!",
"put all your power into a might blow!",
"duck under an incoming strike and lash out in response!"
]

def dead(why):
    print(why, "Your adventure is over!\n")
    exit(0)


def combat(enemy, enemy_hp, enemy_attack, enemy_damage):
    global player_hp, player_attacks

    while enemy_hp > 0:
        player_damage = randint(1, 3)
        print("\nYou face down the", enemy, ".")
        print("\nSeeing your chance you", player_attacks[randint(0, len(player_attacks)-1)])
        enemy_hp -= player_damage
        print(">>>> enemy hp is", enemy_hp)

        if enemy_hp > 0:
            print("\nYour attack lands but the", enemy, "responds with a",
            enemy_attack + ".")
            print("You have taken damage!")
            player_hp -= enemy_damage
            print(">>>> Player hp is", player_hp)
            if player_hp < 0:
                dead("\nYou succumb to your wounds")
            else:
                print("\nThe fight continues!\n")
                input("<Press Enter for the next turn!>")


        else:
            print("\nThe", enemy, "can fight no more. Victory!\n")


if __name__ == "__main__":
    print(">>>> Running as main.")
    player_hp = 10
    sword = "your sword"
    combat("skeleton", 5, "sworld slash", 1)
