## Based on Sailors on the Starless Sea


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
    'on a black field, stands high atop the ruined walls.\nWhatever horror',
    'lurks within has terrorised you and your village for far too long.\n')

    print('You take a deep breath and ready your weapons. The time for',
    'retribution has come. Do you walk the road up to the keep?')

    while True:
        choice = input('> ')

        print(choice)
        if choice == "y" or choice == "yes" or choice == "Yes" or choice == "Y":
            road_to_keep()
            ###Go to road road()

        else:
            print("You stand there catching your breath.",
            "There is only one path forward.")




### -----------------Game----------------------------------------

start()
