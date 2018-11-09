from sys import exit
from combat import combat, player_hp, dead
# from combat import player_hp
# from combat import dead
from random import randint
from textwrap import dedent

player_inventory = []

cache_found = False
charnel_ruins_entered = False
well_visited = False
tower_clear = False
fountain_ooze = False
fled_ooze = False


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

    # and to print the final scene
    # current_scene.enter()


class StairsToDarkness(Scene):
    def enter(self):

        print(dedent("""
        You walk down the spooky stairs. This module is over.
        """))

        exit(1)


class Battlements(Scene):
    def enter(self):

        print(">>>> Entering Battlements")

        print(dedent("""
        You walk up on the battlements. They're not very exciting. You walk
        along them a bit and then see some stairs down to another part of
        the keep.

        Would you like to walk down the stairs?
        """))

        while True:
            choice = input("> ")

            if choice.lower() == "yes" or choice.lower() == "y":

                print(dedent("""
                You head to the stairs going down..
                """))

                return "stairs"

            elif choice.lower() == "no" or choice.lower() == "n":

                print(dedent("""
                You decide to stay on the battlements.

                Where would you like to go?
                """))

            else:

                print(dedent("""
                Seeing no other real option you head back along the battlements
                and down into the tower you came from.
                """))

                return 'tower'


class TowerNav(Scene):
    def enter(self):

        print(">>>> Entering Tower Nav")
        while True:

            print(dedent("""
            You stand in the tower. There are some stairs go up.

            Where would you like to go?
            """))

            choice = input("> ")

            if "leave" in choice.lower() or "courtyard" in choice.lower():

                return 'courtyard'

            elif choice.lower() == "stairs" or choice.lower() == "up":

                return 'battlements'


class TowerOfBeasts(Scene):
    def enter(self):

        global player_hp, tower_clear

        print("\n>>>> Tower of beasts")

        if tower_clear is False:

            print("\nYou see some horrid beastmen")

            combat("beastmen", 10, "display of savage fury!", 2)

            from combat import player_hp

            tower_clear = True

            if player_hp <= 5:
                print("\n>>>> You are badly wounded and should so something")

            elif player_hp >= 6:
                print("\n>>>> You're doing ok.")

            print("\n>>>> Having won you can look around the tower")

            return 'tower nav'

        else:

            print(">>>> You return to the tower")

            return 'tower nav'


class WellOfSouls(Scene):
    def enter(self):

        global well_visited

        if well_visited is False:

            well_visited = True

            print(dedent("""
            A barren ridge of black stone rises from the overgrown courtyard.
            A low stone wall marked with eerie sigils is built atop the crest
            of the stone, marking a well. A stout block and tackle frame
            supports a single thick chain that plunges into the inky blackness.
            A soft moan rises from the well, like a faint cry for help.

            Will you peer into the well?
            """))

            while True:
                choice = input("> ")

                print(">>>>", choice)

                if (choice.lower() == "yes" or choice.lower() == "y"):

                    print(dedent("""
                    You peer over the lip of the well into a gaping abyss. Your
                    mind struggles to comprehend the infinite oblivion before
                    you.
                    """))

                    chance_of_survival = randint(1, 3)

                    print(">>>> Chance of survival =", chance_of_survival)

                    if chance_of_survival == 1:
                        dead("Your mind snaps utterly under the strain.")

                    else:
                        from combat import player_hp
                        player_hp -= 2

                        if player_hp < 0:
                            print(dedent("""
                            In your weakened state you cannot resist the call
                            of oblivion. You slip forwards and fall into
                            the darkness.

                            Forever.
                            """))
                            dead("You fall for an eternity")

                        else:
                            from combat import player_hp
                            print(dedent("""
                            A sense of your own insignificance threatens to
                            overcome you, but you fight it back. This well is
                            evil and you resolve to leave it alone.
                            """))

                            print(">>>> Player hp is", player_hp)

                            return 'courtyard'

                else:
                    print(dedent("""
                    A sense of your own insignificance threatens to
                    overcome you, but you fight it back. This well is
                    evil and you resolve to leave it alone.
                    """))

                    return 'courtyard'

            return 'courtyard'

        else:

            print(dedent("""
            You cannot resist returning to the well. It calls to you and you
            slip forwards and fall into the darkness.
            Forever.
            """))

            dead("You fall for an eternity")

            # return 'courtyard'


class Fountain(Scene):
    def enter(self):

        global fountain_ooze, fled_ooze, player_inventory

        print(">>>> Fountain")

        if fountain_ooze is False:

            print(dedent("""
            As you move forwards you can see that the toad fountain is adorned
            with red gemstone eyes and jeweled fangs within the loathsome maw.
            The ooze in the fountain bubbles and then suddenly lurches
            outwards, animated by some unknown force. Splitting into several
            strange shapes it moves towards you with evil intent...

            What will you do?
            """))

            while True:
                choice = input("> ")

                print(">>>>", choice)

                if (choice.lower() == "attack" or choice.lower() == "fight"):

                    combat("Black Oozlings", 10, "mass of hot tar", 3)

                    print(dedent("""
                    Having escaped with your life you decide you deserve a
                    little reward. You spend half an hour or so prying away at
                    the fountain and make yourself several gemstones richer,
                    before returning to the courtyard.
                    """))

                    fountain_ooze = True

                    player_inventory.append("Red gemstones")

                    return 'courtyard'

                elif "powder" in choice:

                    print(dedent("""
                    You hurl the green powder at the strange oozes. They errupt
                    into flames, thrash around and then melt away.
                    Pleased with yourself you decide you deserve a little
                    reward. You spend half an hour or so prying away at the
                    fountain and make yourself several gemstones richer, before
                    returning to the courtyard.
                    """))

                    fountain_ooze = True

                    player_inventory.append("Red gemstones")

                    return 'courtyard'

                # elif:
                #    choice.lower() == "flee" or choice.lower() == "run":

                #    print(dedent("""
                #    You flee from the ooze, dashing back to the courtyard.
                #    """))

                #    fled_ooze == "True"

                else:
                    print("\nYou attempt to", choice.lower(),
                          "but the enemy is upon you first!")

                    combat("Black Oozlings", 10, "mass of hot tar", 3)

                    print(dedent("""
                    Having escaped with your life you decide you deserve a
                    little reward. You spend half an hour or so prying away at
                    the fountain and make yourself several gemstones richer,
                    before returning to the courtyard.
                    """))

                    fountain_ooze = True

                    player_inventory.append("Red gemstones")

                    return 'courtyard'

        else:
            print("Fortunately there is no ooze!")

            print("\nYou return to the courtyard.")

            return 'courtyard'


class CharnelRuins(Scene):
    def enter(self):
        global charnel_ruins_entered, fountain_ooze


        if charnel_ruins_entered is False:

            print(dedent("""
            This once-proud edifice has fallen into ruin like the rest of the
            keep. All that remains of the building are fire-scarred high stone
            walls and toad-faced gargoyles leering from above. The singed,
            bronze doors—cast with hundreds of wailing demonic faces—are barred
            from the outside. The portal is marked with a single word drawn in
            flaking red paint: 'REPENT')

            You push the fear down inside you and make your way inside.
            """))

            charnel_ruins_entered = True

            print(dedent("""
            Six charred skeletons lie about the chapel, some crushed by burnt
            fallen beams. At the head of the chapel is a fountain depicting a
            squat, demonic toad. A foul, black ichor seeps from the toad’s
            broad lips, pooling in the basin seated at the foot of the
            fountain.

            It is clear this slaughter happened long ago, but the stench of
            charred flesh lingers in the hot air.

            Would you like to investigate further, or leave?
            """))

            while True:
                choice = input("> ")

                print(">>>>", choice)

                if (choice.lower() == "y" or choice.lower() == "yes" or
                    choice.lower() == "investigate"):

                    return 'fountain'

                else:
                    print("\nYou return to the courtyard.")

                    return 'courtyard'

        else:
            print("\nYou return to the charred chapel")

            if fountain_ooze is False:

                print(dedent("""
                Six charred skeletons lie about the chapel, some crushed by
                burnt fallen beams. At the head of the chapel is a fountain
                depicting a squat, demonic toad. A foul, black ichor seeps from
                the toad’s broad lips, pooling in the basin seated at the foot
                of the fountain.

                It is clear this slaughter happened long ago, but the stench of
                charred flesh lingers in the hot air.

                Would you like to investigate further, or leave?"""))

                while True:
                    choice = input("> ")

                    print(">>>>", choice)

                    if (choice.lower() == "y" or choice.lower() == "yes" or
                        choice.lower() == "investigate"):

                        return 'fountain'

                    else:
                        print("\nYou return to the courtyard.")

                        return 'courtyard'

                else:

                    print(dedent("""
                    Having already investigated the chapel you return to the
                    courtyard.
                    """))

                    return 'courtyard'


class Cache(Scene):
    def enter(self):
        global cache_found, player_inventory

        print("\n>>>> Hidden cache")

        if cache_found is False:

            print(dedent("""
            Taking a careful look around you notice muddy footprints; the
            tracks of man-sized creatures with hawklike talons.

            Pulling away the dead brambles and matted weeds, you find a long
            flagstone, half-buried in the muddy ground. Digging away the
            rotting soil you are able to prise it up, revealing a secret
            cache hidden beneath it.

            A hide wrapped bundle has been secreted here. Unwrapping it you
            discover a strange small stone idol depicting a many faced being.
            Alongside it is a leather poch containing a strange green power.
            You take these items for yourself.
            """))

            player_inventory.append("Stone Idol")
            player_inventory.append("Green Powder")

            print("\nYou are currently carrying", player_inventory)

            cache_found = True

            return 'courtyard'

        else:
            print(dedent("""
            You almost stub your toe on the flagstone you pulled up but there's
            no more treasure to be found here!
            """))

            return 'courtyard'


class Courtyard(Scene):
    def enter(self):

        print(dedent("""
        The courtyard is overgrown with sickly weeds and thick bramblesself.
        A deathly silence hangs in the air, as if even the frogs and insects
        are afraid to draw attention to themselves. The smell of rotting
        vegetation is pervasive, and the ground sucks at your boots with
        every tentative step.

        Nearly all of the courtyard’s buildings have fallen into ruin. A single
        burnt-out shell set against the keep’s east wall is the only remaining
        structure. Set near the heart of the courtyard is a well, framed with a
        crude pulley system. Off to the south-east is the keep’s sole
        standing tower.

        Where would you like to go?
        """))

        while True:
            choice = input("> ")

            if choice.lower() == "gate" or choice.lower() == "gatehouse":

                print(dedent("""
                You return to the keep's entrance, but with the portcullis down
                you can see no easy way to exit. You retrace your steps.
                """))

                return 'courtyard'

            elif "well" in choice.lower() or "heart" in choice.lower():

                return 'well'

            elif choice.lower() == "east" or choice.lower() == "structure":

                return 'ruins'

            elif (choice.lower() == "south-east" or
                  choice.lower() == "south east" or
                  "tower" in choice.lower()):

                return 'tower'

            elif ("look" or "search") in choice.lower():

                return 'cache'

            else:

                print(dedent("""
                You aren't sure how to get there.")
                Where would you like to go?
                """))


class Portcullis(Scene):
    def enter(self):

        global player_hp

        print(dedent("""
        As you duck under the portcullis there is a horrible  bestial howling
        from above and the portcullis comes crashing down on you!
        """))

        chance_of_survival = randint(1, 3)

    #    print(">>>> Chance of survival =", chance_of_survival)

        if chance_of_survival == 1:
            dead("The portcullis crushes you to death.")

        else:
            player_hp -= 2

            if player_hp < 0:
                print(dedent("""
                You are pinned by the portcullis.
                Your existing wounds are made worse.
                """))
                dead("You bleed out.")

            else:
                print(dedent("""
                The portculis rakes your back, but you just manage to make it
                to the other side without being crushed.
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

        The ancient drawbridge has long since fallen away into ruin, leaving
        only a few rotting planks placed across the ditch. The heavy iron
        portcullis stands half-raised, the rusty spikes a mere four feet above
        slots cut into the stone floor.
        """))

        print("\nDo you wish to enter, ducking under the portcullis?")

        while True:
            choice = input('> ')

            if choice.lower() == "y" or choice.lower() == "yes":
                print(dedent("""
                You crouch down and attempt to ease your way in under the
                portcullis.
                """))
                return 'portcullis'

            elif (choice.lower() == "n" or choice.lower() == "no" or
                  choice.lower() == "listen" or choice.lower == "look"):

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
                print(dedent("""
                You run in terror. You are not the hero you hoped you were!
                """))
                dead("You fled")

            else:
                print("You can't see a way to do that.")


class BlacksmithSons(Scene):
    def enter(self):

        print(dedent("""
        Outside of heat of battle you are able to recognise the corpses as the
        bodies of young Algor and Eldin, the sons of the village blacksmith
        stolen from their home seven nights ago. The foul vines have desicrated
        their bodies.

        Investigating further you find a small signet ring on the
        hand of Eldin.You take it, resolving to return it to their father.
        """))

        player_inventory.append("Signet ring")
        print("\nSignet ring added to inventory. You are currently carring",
              player_inventory)

        print("With a heavy heart you continue down the road to the keep.")

        return 'gatehouse'


class RoadToKeep(Scene):
    def enter(self):
        print(dedent("""
        As you walk down the road you take stock of your situation.
        You are the only one in your village brave enough to strike against
        the evil that steals your kinfolk in the night. You alone hold the
        blade known to the world as...
        """))

        global sword
        sword = input('> ')
        player_inventory.append(sword)

        print("\nIndeed, the mighty sword", sword, "gives you strength.",
              "You know you must prevail. For the sake of your village.")

        print(dedent("""
        You come to a stop. A grisly sight bars your way: a pair of corpses,
        secured to poles by long ropey vines.The foul vegitation has wormed its
        way inside the bodies' eyes, ears, and mouths. To your horror, you
        realize the bodies are still moving...

        Do you attack the twitching corpses, or flee in terror?
        """))

        choice = input('> ')

        if "attack" in choice.lower() or "fight" in choice.lower():

            print("You fight!")
            combat("vine corpses", 7, "thorny clawed fist", 1)
            from combat import player_hp

            return 'sons'

        elif "flee" in choice.lower() or "run" in choice.lower():

            print(dedent("""
            You flee in terror. You are not the hero you hoped you were!
            """))
            dead("You fled")

        else:
            print("\nYou attempt to", choice.lower(),
                  "but the enemy is upon you first!")

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
            forgotten battles and the clash of mighty armies. Now the ruins
            seem host only to creeping vines and the foul miasma that drifts
            down from the keep.

            The air is overun with pestilence. Fat flies bite at you
            incessantly, and clouds of small black insects choke your every
            breath.

            The long-abandoned land is strangled with thorny vines that drape
            the sickly trees and hang from the ruined walls. There is an odor
            of rot and decay, as if the hill itself were decomposing from
            within.

            A sight gives you pause: a ragged banner, depciting a crimson skull
            on a black field, stands high atop the ruined walls.

            You take a deep breath and ready your weapons. The time for
            retribution has come. Whatever horror lurks within has terrorised
            you and your village for far too long.
            """))

        print(dedent("""
        An old dirt road, now overrun with weeds and sickly vines, rises
        towards the ruined citadel.

        Do you walk the road up to the keep?
        """))

        while True:
            choice = input('> ')

            if choice.lower() == "y" or choice.lower() == "yes":
                return 'road'
                # Go to road road()

            else:
                print(dedent("""
                You stand there catching your breath There is only one path
                forward.
                """))


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
            'well': WellOfSouls(),
            'tower': TowerOfBeasts(),
            'tower nav': TowerNav(),
            'cache': Cache(),
            'ruins': CharnelRuins(),
            'fountain': Fountain(),
            'battlements': Battlements(),
            'stairs': StairsToDarkness(),
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
