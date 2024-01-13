from Human import Human
from Robot import Robot
class Planet:
    def __init__(self, name):
        self.humans = []
        self.robots = []
        self.name = name

    def add_human(self, human):
        self.humans.append(human)

    def remove_human(self, human):
        if human in self.humans:
            self.humans.remove(human)

    def add_robot(self, robot):
        self.robots.append(robot)

    def remove_robot(self, robot):
        if robot in self.robots:
            self.robots.remove(robot)

    def __repr__(self):
        return f"Planet(name={self.name}, humans={self.humans}, robots={self.robots})"

    def __str__(self):
        human_names = [human.name for human in self.humans]
        robot_names = [robot.name for robot in self.robots]
        return (f"Planet {self.name}:\n"
                f"  Humans: {', '.join(human_names) if human_names else 'None'}\n"
                f"  Robots: {', '.join(robot_names) if robot_names else 'None'}")


if __name__ == "__main__":
    earth = Planet("Earth")

    human1 = Human()
    human2 = Human()
    robot1 = Robot()
    robot2 = Robot()

    earth.add_human(human1)
    earth.add_human(human2)
    earth.add_robot(robot1)
    earth.add_robot(robot2)

    earth.remove_human(human2)
    earth.remove_robot(robot2)

    print(repr(earth))
    print(str(earth))
