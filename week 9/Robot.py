class Robot:
    laws = "Protect, Obey and Survive"
    MAX_ENERGY = 100

    def __init__(self, name="Robot"):
        self.name = name
        self.age = 0
        self.energy = 0

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f"Robot(name={self.name}, age={self.age}, energy={self.energy})"

    def __str__(self):
        return f"{self.name} (Age: {self.age}, Energy: {self.energy})"

    def grow(self):



    def eat(self, amount):



    def move(self, distance):


if __name__ == "__main__":
    robot = Robot()
    robot.grow()
    robot.eat(10)
    robot.move(5)
    print(str(robot))
