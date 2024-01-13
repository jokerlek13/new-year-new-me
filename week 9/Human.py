class Human:
    MAX_ENERGY = 100

    def __init__(self):
        self.name = "Human"
        self.age = 0
        self.energy = Human.MAX_ENERGY

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"Human(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Energy: {self.energy})"

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy = min(self.energy + amount, Human.MAX_ENERGY)

    def move(self, distance):
        self.energy = max(self.energy - distance, 0)

if __name__ == "__main__":
    human = Human()
    human.grow()
    human.eat(10)
    human.move(5)
    print(str(human))
