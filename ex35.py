from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    #if "0" in choice or "1" in choice: - new way is better
    if choice.isnumeric():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much <50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "fight bear":
            dead("The bear easily defeats you, killing you horribly.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through the door now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your own head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well, that was tasty!")
    else:
        cthulhu_room()


def rug_room():
    print("You lift up the rug to discover a strange hole.")
    print("As you gaze down into it you lose your footing and fall in!")
    print("You crash land deep in the dark.")
    print("Do you look for way out or stay here in the dark?")

    while True:

        choice = input("> ")

        if "out" in choice:
            print("You crawl onwards and step through a magic honey portal",
            "into a new room.")
            bear_room()
        elif "stay" in choice:
            dead("You stay in the dark and eventually starve to death.")
        else:
            print("You might want to try something else...")



def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left. An ugly rug is on the floor.")
    print("Which door do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "rug":
        rug_room()
    else:
        dead("You stumble around the room until you starve.")


start()
