## Based on Sailors on the Starless Sea
from random import randint
from sys import exit


player_inventory = []
player_hp = 10
player_damage = randint(0, 3)

def dead(why):
    print(why, "Your adventure is over!\n")
    exit(0)

def combat(enemy, enemy_hp, enemy_attack, enemy_damage):
    global sword
    global player_hp
    while enemy_hp > 0:
        player_damage = randint(1, 3)
        print("\nYou face down the", enemy, "with", sword, "in your hand.")
        print("\nSeeing your chance you lunge forwards and strike a blow!")
        enemy_hp -= player_damage
        print(">>>> enemy hp is", enemy_hp)

        if enemy_hp > 0:
            print("\nYour attack lands but the", enemy, "respond with a",
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


def stairs_to_darkness():
    print("\nStairs to darkness and end")

def battlements():
    print("\n>>>> Battlements")

def tower_of_beasts():
    print("\n>>>> Tower of beasts")

def sinkhole():
    print("\n>>>> Sinkhole")

def well_of_souls():
    print("\n>>>> Well of souls")

def charnel_ruins():
    print("\n>>>> Charnel Ruins")

#cache
def cache():
    print("\n>>>> Hidden cache")

# courtyard
def courtyard():
    print("\n>>>> Courtyard")

def portcullis():
    global player_hp
    print("\n>>>> Portculis falls")

    print("\nAs you duck under the portcullis there is a horrible bestial howling",
    "from above and the portcullis comes crashing down on you!")

    chance_of_survival = randint(1, 3)

    print(">>>> Chance of survival =", chance_of_survival)

    if chance_of_survival == 1:
        dead("The portcullis crashes down on you, crushing you to death.")

    else:
        player_hp -= 2

        if player_hp < 0:
            print("\nYou are pinned by the portcullis.",
            "Your existing wounds are made worse.")
            dead("You bleed out.")

        else:
            print("\nThe portculis rakes your back, but you just manage to make",
            "it to the other side without being crushed.")

            print(">>>> Player hp is", player_hp)

            gatehouse()

# gatehouse
def gatehouse():
    print("\n>>>> Gatehouse")

    print("\nThe dark, moss-eaten gatehouse towers above you, grim and forbidding.",
    "Murder holes, fashioned in the likeness of looming toads, threaten to gout",
    "forth flaming oil and tar. Black arrow slits pierce the high stone walls."
    " You can hear the flap of the heretical banner above, hidden from sight by",
     "the vine-draped battlements.")

    print("\nThe ancient drawbridge has long since fallen away into ruin, leaving",
     "only a few rotting planks placed across the ditch. The heavy iron",
     "portcullis stands half-raised, the rusty spikes a mere four feet above",
     "slots cut into the stone floor.")

    print("\nDo you wish to enter, ducking under the portcullis?")

    while True:
        choice = input('> ')

        if choice.lower() == "y" or choice.lower() == "yes":
            print("\nYou crouch down and attempt to ease your way in under the",
            "portcullis")
            portcullis()

        elif (choice.lower() == "n" or choice.lower() == "no"
        or choice.lower() == "listen" or choice.lower == "look"):

            print("\nYou pause, sensing danger. You focus your senses and take note",
            "of an animalistic sniffling sound and the scratch of claws on stone",
            "coming from the gatehouse above.")
            print("\nRealising the threat you hurl yourself at great speed under the",
            "wicked spikes. You reach the other side and the portculis slams shut",
            "behind you. A great bell tolls from inside the gatehouse. The enemy",
            "knows you are here, but you have evaded their trap")

            print("\nThe keep's courtyard stretches out before you.")

            courtyard()

        elif "flee" in choice.lower() or "run" in choice.lower():
            print("You run in terror. You are not the hero you hoped you were!\n")
            dead("You fled")

        else:
            print("You can't see a way to do that.")

# road to the keep
def road_to_keep():
    print(">>>> Road to keep")

    print('\n As you walk down the road you take stock of your situation.')
    print('You are the only one in your village brave enough to strike against',
    'the evil that steals your kinfolk in the night.')
    print('You alone hold the blade known to the world as...\n')

    global sword
    sword = input('> ')
    player_inventory.append(sword)

    print("\nIndeed, the mighty sword", sword, "gives you strength.",
    "You know you must prevail. For the sake of your village.")

    print("\nYou come to a stop.")
    print("\nA grisly sight bars your way: a pair of bodies, secured to poles by",
    "long ropey vines.")
    print("Wicked vines have wormed their way inside the bodies’", "eyes,"
    " ears, and mouths.")
    print("\nTo your horror, you realize the bodies are still moving...")
    print("\nDo you attack the twitching corpses, or flee in terror?")

    choice = input('> ')

    if "attack" in choice.lower() or "fight" in choice.lower():
        print("You fight!")
        combat("vine corpses", 7, "thorny clawed fist", 1)

        print("Outside of heat of battle you are able to recognise the corpses",
        "as the bodies of young Algor and Eldin, the sons of the village",
        "blacksmith stolen from their home seven nights ago.")
        print("\n The foul vines have desicrated their bodies. Investigating",
        "further you find a small signet ring on the hand of Eldin.\nYou take",
        "it resolving to return it to their father.")

        player_inventory.append("Signet ring")
        print("\n Signet ring added to inventory. You are currently carring",
         player_inventory)

        print("With a heavy heart you continue down the road to the keep.")

        gatehouse()

    elif "flee" in choice.lower() or "run" in choice.lower():
        print("You run in terror. You are not the hero you hoped you were!\n")
        dead("You fled")

    else:
        print("\nYou attempt to",choice.lower(), "but the enemy is upon you first!")
        global player_hp
        player_hp -= 1
        print("\nDead limbs and thorns cut and wound you!")

# Start of the game
def start():
    global player_inventory

    print('\nYou stand before a ruined keep which squats atop a low craggy hill.')
    print('Its walls of toppled stone and massive granite blocks hint at',
    'forgotten battles and the clash of mighty armies.')
    print('Now the ruins seem host only to creeping vines and the foul miasma',
    'that drifts down from the keep.\n')

    print('The air is overun with pestilence.')
    print('Fat flies bite at you incessantly, and clouds of small black insects',
    'choke your every breath.')
    print('The long-abandoned land is strangled with thorny vines that drape',
    'the sickly trees and hang from the ruined walls.')
    print('There is an odor of rot and decay, as if the hill itself were',
    'decomposing from within.\n')

    print('A sight gives you pause: a ragged banner, depciting a crimson skull',
    'on a black field, stands high atop the ruined walls.')

    print('You take a deep breath and ready your weapons. The time for',
    'retribution has come.')
    print('Whatever horror lurks within has terrorised you and your village',
    'for far too long.')
    print("\nAn old dirt road, now overrun with weeds and sickly vines, rises",
    "towards the ruined citadel.")
    print('\nDo you walk the road up to the keep?')

    while True:
        choice = input('> ')

        if choice.lower() == "y" or choice.lower() == "yes":
            road_to_keep()
            ###Go to road road()

        else:
            print("You stand there catching your breath.",
            "There is only one path forward.")




### -----------------Game----------------------------------------

start()
