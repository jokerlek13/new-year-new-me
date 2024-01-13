class Inhabitant:
    MAX_ENERGY = 100

    def __init__(self, name="Inhabitant", age=0, energy=MAX_ENERGY):
        self.name = name
        self.age = age
        self.energy = energy

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Energy: {self.energy})"


    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy = min(self.energy + amount, Inhabitant.MAX_ENERGY)

    def move(self, distance):
        self.energy = max(self.energy - distance, 0)

