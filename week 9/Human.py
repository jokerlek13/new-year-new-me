class Human:
    # Class attribute
    MAX_ENERGY = 100

    # Initializer
    def __init__(self, name="Human", age=0, energy=None):
        self.name = name
        self.age = age
        self.energy = Human.MAX_ENERGY if energy is None else energy

    # Instance method
    def display(self):
        print(f"I am {self.name}")

# Testing the Human class
if __name__ == "__main__":
    human = Human()
    human.display()
In this class: