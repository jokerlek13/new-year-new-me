class Robot:
    # Class attribute
    laws = "Protect, Obey and Survive"
    MAX_ENERGY = 100

    # Static method
    @staticmethod
    def the_laws():
        print(Robot.laws)

    # Class method
    @classmethod
    def assemble(cls):
        return cls("Assembled Robot")

    # Initializer
    def __init__(self, name="Robot", energy=0):
        self.name = name
        self.age = 0
        self.energy = energy

    # Instance method
    def display(self):
        print(f"I am {self.name}")

# Testing the Robot class
if __name__ == "__main__":
    robot = Robot()
    robot.display()
