## Based on Sailors on the Starless Sea
player_inventory = []

player_hp = 10

def stairs_to_darkness():
    print("Stairs to darkness and end")

def battlements():
    print(">>>> Battlements")

def tower_of_beasts():
    print(">>>> Tower of beasts")

def sinkhole():
    print(">>>> Sinkhole")

def well_of_souls():
    print(">>>> Well of souls")

def charnel_ruins():
    print(">>>> Charnel Ruins")

#cache
def cache():
    print(">>>> Hidden cache")

# courtyard
def courtyard():
    print(">>>> Courtyard")

# gatehouse
def gatehouse():
    print(">>>> Gatehouse")

# road to the keep
def road_to_keep():
    print(">>>> Road to keep")

    print('\n As you walk down the road you take stock of your situation.')
    print('You are the only one in your village brave enough to strike against',
    'the evil that steals your kinfolk in the night.')
    print('You alone hold the blade known to the world as...\n')

    sword = input('> ')
    player_inventory.append(sword)

    print("\nIndeed, the mighty sword", sword, "gives you strength.",
    "You know you must prevail. For the sake of your village.")

    print("\nYou come to a stop.")
    print("\nA grisly sight bars your way: a pair of bodies, secured to poles by",
    "long ropey vines.")
    print("Wicked vines have wormed their way inside the bodies’", "eyes,"
    "ears, and mouths.")
    print("\nTo your horror, you realize the bodies are still moving...")
    print("\nDo you attack the twitching corpses, or flee in terror?")

    choice = input('> ')

    if "attack" in choice.lower() or "fight" in choice.lower():
        print("You fight!")
    elif "flee" in choice.lower() or "run" in choice.lower():
        print("You run!")
    else:
        print("\nYou attempt to",choice.lower(), "but the enemy is upon you first!")
        global player_hp
        player_hp -= 1
        print("\nDead limbs and thorns cut and wound you!")

# Start of the game
def start():
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
