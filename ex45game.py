from sys import exit
from combat import combat
from combat import player_hp
from combat import dead
from random import randint
from textwrap import dedent

player_inventory = []

class Scene(object):

    def enter(self):
        print("\n This scene", self, "has not been implimented yet.")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

    #and to print the final scene
    #current_scene.enter()

class StairsToDarkness(Scene):
    def enter(self):
        pass

class Battlements(Scene):
    def enter(self):
        pass

class TowerNav(Scene):
    def enter(self):
        pass

class TowerOfBeasts(Scene):
    def enter(self):
        pass

class WellOfSouls(Scene):
    def enter(self):
        pass

class CharnelRuins(Scene):
    def enter(self):
        pass

class Cache(Scene):
    def enter(self):
        pass

class Courtyard(Scene):
    def enter(self):
        print("Courtyard")
        pass

class Portcullis(Scene):
    def enter(self):

        global player_hp
        print("\n>>>> Portculis falls")


        print(dedent("""
        As you duck under the portcullis there is a horrible  bestial howling
        from above and the portcullis comes crashing down on you!
        """))

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
                print(dedent("""
                The portculis rakes your back, but you just manage to make it to
                the other side without being crushed.
                """))

                print(">>>> Player hp is", player_hp)

                return 'courtyard'


class Gatehouse(Scene):
    def enter(self):

        print(dedent("""
        The dark, moss-eaten gatehouse towers above you, grim and forbidding.
        Murder holes, fashioned in the likeness of looming toads, threaten to
        gout forth flaming oil and tar. Black arrow slits pierce the high stone
        walls You can hear the flap of the heretical banner above, hidden from
        sight by the vine-draped battlements.

        The ancient drawbridge has long since fallen away into ruin, leaving only
        a few rotting planks placed across the ditch. The heavy iron portcullis
        stands half-raised, the rusty spikes a mere four feet above slots cut
        into the stone floor.
        """))

        print("\nDo you wish to enter, ducking under the portcullis?")

        while True:
            choice = input('> ')

            if choice.lower() == "y" or choice.lower() == "yes":
                print("\nYou crouch down and attempt to ease your way in under the",
                "portcullis")
                return 'portcullis'

            elif (choice.lower() == "n" or choice.lower() == "no"
            or choice.lower() == "listen" or choice.lower == "look"):

                print(dedent("""
                You pause, sensing danger. You focus your senses and take note
                of an animalistic sniffling sound and the scratch of claws on
                stone coming from the gatehouse above.

                Realising the threat you hurl yourself at great speed under the
                wicked spikes. You reach the other side and the portculllis
                slams shut behind you. A great bell tolls from inside the
                gatehouse. The enemy knows you are here, but you have evaded
                their trap.

                The keep's courtyard stretches out before you.
                """))

                return 'courtyard'

            elif "flee" in choice.lower() or "run" in choice.lower():
                print("You run in terror. You are not the hero you hoped you were!\n")
                dead("You fled")

            else:
                print("You can't see a way to do that.")


class BlacksmithSons(Scene):
    def enter(self):

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

        return 'gatehouse'


class RoadToKeep(Scene):
    def enter(self):
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
            from combat import player_hp

            return 'sons'

        elif "flee" in choice.lower() or "run" in choice.lower():
            print("You run in terror. You are not the hero you hoped you were!\n")
            dead("You fled")

        else:
            print("\nYou attempt to",choice.lower(), "but the enemy is upon you first!")
            global player_hp
            player_hp -= 1
            print("\nDead limbs and thorns cut and wound you!")
            combat("vine corpses", 7, "thorny clawed fist", 1)
            from combat import player_hp

            return 'sons'

class Start(Scene):

    def enter(self):
        print(dedent("""
            You stand before a ruined keep which squats atop a low craggy hill.
            Its walls of toppled stone and massive granite blocks hint at
            forgotten battles and the clash of mighty armies. Now the ruins seem
            host only to creeping vines and the foul miasma that drifts down
            from the keep.

            The air is overun with pestilence. Fat flies bite at you
            incessantly, and clouds of small black insects choke your every
            breath. Fat flies bite at you incessantly, and clouds of small black
            insects choke your every breath.

            The long-abandoned land is strangled with thorny vines that drape the
             sickly trees and hang from the ruined walls. There is an odor of
             rot and decay, as if the hill itself were decomposing from within.

             A sight gives you pause: a ragged banner, depciting a crimson skull
             on a black field, stands high atop the ruined walls.

             You take a deep breath and ready your weapons. The time for
             retribution has come. Whatever horror lurks within has terrorised
             you and your village for far too long.
             """))

        print("\nAn old dirt road, now overrun with weeds and sickly vines, rises",
        "towards the ruined citadel.")
        print('\nDo you walk the road up to the keep?')

        while True:
            choice = input('> ')

            if choice.lower() == "y" or choice.lower() == "yes":
                return 'road'
                ###Go to road road()

            else:
                print("You stand there catching your breath.",
                "There is only one path forward.")

class Finished(Scene):
    pass

class Map(object):

    scenes = {
    'start': Start(),
    'road': RoadToKeep(),
    'sons': BlacksmithSons(),
    'gatehouse': Gatehouse(),
    'portcullis': Portcullis(),
    'courtyard': Courtyard(),
    'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('start')
a_game = Engine(a_map)
a_game.play()
