class LandAnimal:
    def walk(self):
        print('walk')

class WaterAnimal:
    def swim(self):
        print('swim')

class Amphibian(LandAnimal, WaterAnimal):
    pass

frog = Amphibian()

frog.swim()
frog.walk()

class Planet:
    pass

earth = Planet()

earth.__repr__()

