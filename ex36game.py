## Based on Sailors on the Starless Sea
from random import randint
from sys import exit


player_inventory = []
player_hp = 12
player_damage = randint(0, 3)

cache_found = False
charnel_ruins_entered = False
well_visited = False
tower_clear = False
fountain_ooze = False

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


player_damage = randint(0, 3)

def dead(why):
    print(why, "Your adventure is over!\n")
    exit(0)

def stairs_to_darkness():
    print("\nStairs to darkness and end")

def battlements():
    print("\n>>>> Battlements")

def tower_nav():
    print(">>>> Entering Tower Nav")
    while True:
        choice = input("> ")

        if "leave" in choice.lower() or "courtyard" in choice.lower():
            courtyard()

        elif choice.lower() == "stairs":
            battlements()


def tower_of_beasts():
    global player_hp, tower_clear

    print("\n>>>> Tower of beasts")

    if tower_clear == False:

        print("\nYou see some horrid beastmen")

        combat("beastmen", 10, "display of savage fury!", 2 )

        tower_clear = True

        if player_hp <= 5:
            print("\n>>>> You are badly wounded and should so something")

        elif player_hp >= 6:
            print("\n>>>> You're doing ok.")


        print("\n>>>> Having won you can look around the tower")

        tower_nav()

    else:

        print(">>>> You return to the tower")

        tower_nav()



def well_of_souls():
    global well_visited
    print("\n>>>> Well of souls")

    if well_visited == False:

        well_visited = True

        print("You visit the well for the first time")

    else:

        print("You visit the well again.")

def fountain():
    global fountain_ooze, player_inventory
    print(">>>> Fountain")

    if fountain_ooze == False:
        print("Watch out for the oozes!")

        combat("Black Oozlings", 10, "mass of hot tar", 2)

        print("\nHaving escaped with your life you return to the courtyard")
        courtyard()


    else:
        print("Fortunately there is no ooze!")

        print("\nYou return to the courtyard.")
        courtyard()


def charnel_ruins():
    global charnel_ruins_entered, fountain_ooze
    print("\n>>>> Charnel Ruins")

    if charnel_ruins_entered == False:

        print("\nThis once-proud edifice has fallen into ruin like the rest of",
        "the keep. All that remains of the building are fire-scarred high stone",
        "walls and toad-faced gargoyles leering from above.")

        print("\nThe singed, bronze doors—cast with hundreds of wailing demonic",
        "faces—are barred from the outside. The portal is marked with a single",
        "word drawn in flaking red paint: REPENT")

        print("\nYou push the fear down inside you and make your way inside.")

        charnel_ruins_entered = True

        print("\nSix charred skeletons lie about the chapel, some crushed by",
        "burnt fallen beams. At the head of the chapel is a fountain depicting",
        "a squat, demonic toad. A foul, black ichor seeps from the toad’s",
        "broad lips, pooling in the basin seated at the foot of the fountain.")

        print("\nIt is clear this slaughter happened long ago, but the stench",
        "of charred flesh lingers in the hot air.")

        print("\nWould you like to investigate further, or leave?")

        while True:
            choice = input("> ")

            print(">>>>", choice)

            if (choice.lower() == "y" or choice.lower() == "yes"
            or choice.lower() == "investigate"):
                fountain()

            else:
                print("\nYou return to the courtyard.")
                courtyard()






    else:

        print("\n You return to the charred chapel")

        if fountain_ooze == False:

            print("\nSix charred skeletons lie about the chapel, some crushed by",
            "burnt fallen beams. At the head of the chapel is a fountain depicting",
            "a squat, demonic toad. A foul, black ichor seeps from the toad’s",
            "broad lips, pooling in the basin seated at the foot of the fountain.")

            print("\nIt is clear this slaughter happened long ago, but the stench",
            "of charred flesh lingers in the hot air.")

            print("\nWould you like to investigate further, or leave?")

            while True:
                choice = input("> ")

                print(">>>>", choice)

                if (choice.lower() == "y" or choice.lower() == "yes"
                or choice.lower() == "investigate"):
                    fountain()

                else:
                    print("\nYou return to the courtyard.")
                    courtyard()

            else:

                print("\nHaving already investigated the chapel you return to",
                "the courtyard.")
                courtyard()




#cache
def cache():
    global cache_found, player_inventory
    print("\n>>>> Hidden cache")

    if cache_found == False:
        print("\nTaking a careful look around you notice muddy footprints; the",
        "tracks of man-sized creatures with hawklike talons.")

        print("\nPulling away the dead brambles and matted weeds, you find a",
        "long flagstone, half-buried in the muddy ground. Digging away the",
        "rotting soil you are able to prise it up, revealing a secret cache",
        "hidden beneath it")

        print("\nA hide wrapped bundle has been secreted here. Unwrapping it you",
        "discover a strange small stone idol depicting a many faced being.",
        "Alongside it is a leather poch containing a strange green power")

        print("\nYou take these items for yourself.")


        player_inventory.append("Stone Idol")
        player_inventory.append("Green Powder")

        print("\nYou are currently carrying", player_inventory)


        cache_found = True

        print("\nWhere would you like to go?")

    else:
        print("\nYou almost stub your toe on the flagstone you pulled up but",
        "there's no more treasure to be found here!")

        print("\nWhere would you like to go?")

# courtyard
def courtyard():
    print("\n>>>> Courtyard")

    print("\nThe courtyard is overgrown with sickly weeds and thick brambles.",
    "A deathly silence hangs in the air, as if even the frogs and insects are",
    "afraid to draw attention to themselves.""The smell of rotting vegetation",
    "pervasive, and the ground sucks at your boots with every tentative step.")

    print("\nNearly all of the courtyard’s buildings have fallen into ruin. A single",
    "burnt-out shell set against the keep’s east wall is the only remaining",
    "structure. Set near the heart of the courtyard is a well, framed with",
    "a crude pulley system. To the south-east is the keep’s sole standing tower.")

    print("\nWhere would you like to go?")

    while True:
        choice = input("> ")

        if choice.lower() == "gate" or choice.lower() == "gatehouse":

            print("\nYou return to the keep's entrance, but with the portcullis",
            "down you can see no easy way to exit. You retrace your steps.")

            courtyard()

        elif "well" in choice.lower() or "heart" in choice.lower():

            well_of_souls()

        elif choice.lower() == "east" or choice.lower() == "structure":

            charnel_ruins()

        elif (choice.lower() == "south-east" or choice.lower() == "south east"
        or "tower" in choice.lower()):

            tower_of_beasts()

        elif ("look" or "search") in choice.lower():

            cache()

        else:

            print("\nYou aren't sure how to get there")

            print("\nWhere would you like to go?")




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

            courtyard()

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

def blacksmith_sons():

    print("Outside of heat of battle you are able to recognise the corpses",
    "as the bodies of young Algor and Eldin, the sons of the village",
    "blacksmith, stolen from their home seven nights ago.")
    print("\n The foul vines have desicrated their bodies. Investigating",
    "further you find a small signet ring on the hand of Eldin.\nYou take",
    "it resolving to return it to their father.")

    player_inventory.append("Signet ring")
    print("\n Signet ring added to inventory. You are currently carring",
     player_inventory)

    print("With a heavy heart you continue down the road to the keep.")

    gatehouse()

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

        blacksmith_sons()

    elif "flee" in choice.lower() or "run" in choice.lower():
        print("You run in terror. You are not the hero you hoped you were!\n")
        dead("You fled")

    else:
        print("\nYou attempt to",choice.lower(), "but the enemy is upon you first!")
        global player_hp
        player_hp -= 1
        print("\nDead limbs and thorns cut and wound you!")
        combat("vine corpses", 7, "thorny clawed fist", 1)

        blacksmith_sons()

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
#charnel_ruins()
