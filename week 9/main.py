from Human import Human
from Robot import Robot
from Planet import Planet

if __name__ == '__main__':
    print(Human.MAX_ENERGY)

    beautiful_human = Human()
    beautiful_human.display()
    print(beautiful_human)

    clever_robot = Robot()
    clever_robot.display()

    earth = Planet("Earth")
    earth.add_human(beautiful_human)
    earth.add_robot(clever_robot)

    print(earth)
