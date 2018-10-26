class Song(object):

    def __init__(self, lyrics, name):
        self.lyrics = lyrics
        self.name = name

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def song_name(self):
        print("\nThis song is called", self.name)


happy_bday = Song(["\nHappy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"],
                   "Happy Birthday")

bulls_on_parade = Song(["\nThey rally around tha family",
                        "With pockets full of shells"],
                        "Bulls on Parade")

twinkle_twinkle = Song(["\nTwinkle twinkle little star",
                        "How I wonder what you are"],
                        "Twinke Twinle Little Star")

london_bridge_lyrics = ["\nLondon bridge is falling down",
                        "Falling down. Falling down.",
                        "London bridge is falling down.",
                        "My fair lady"]

london_bridge = Song(london_bridge_lyrics, "London Bridge is Falling Down")

happy_bday.song_name()
happy_bday.sing_me_a_song()

bulls_on_parade.song_name()
bulls_on_parade.sing_me_a_song()

twinkle_twinkle.song_name()
twinkle_twinkle.sing_me_a_song()

london_bridge.song_name()
london_bridge.sing_me_a_song()
