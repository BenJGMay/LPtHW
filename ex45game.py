from sys import exit

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
    pass

class Battlements(Scene):
    pass

class TowerNav(Scene):
    pass

class TowerOfBeasts(Scene):
    pass

class WellOfSouls(Scene):
    pass

class CharnelRuins(Scene):
    pass

class Cache(Scene):
    pass

class Cortyard(Scene):
    pass

class Portcullis(Scene):
    pass

class Gatehouse(Scene):
    pass

class RoadToKeep(Scene):
    pass

class Start(Scene):

    def enter(self):
        return 'road'

class Finished(Scene):
    pass

class Map(object):

    scenes = {
    'start': Start(),
    'road': RoadToKeep(),
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
