import matplotlib.pyplot as plt

def small():
    x = [3, 10, 10, 3]
    y = [3, 3, 10, 10]
    plt.plot(x, y)
    plt.title('Small Plot')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.show()

def medium():
    x = [2, 5, 5, 2, 2]
    y = [2, 2, 5, 5, 2]
    plt.plot(x, y, 'gs--')
    plt.title('Medium Plot')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.show()

def large():
    x = [1, 4, 4, 7, 7, 4, 4, 1, 1]
    y = [1, 1, 4, 4, 7, 7, 4, 4, 1]
    plt.plot(x, y, 'ro-')
    plt.title('Large Plot')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.show()

def coordinate():-
    x = float(input("Enter an x value: "))-
    y = float(input("Enter a y value: "))
    return (x, y)

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []

    for _ in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return [x_values, y_values]

def run_task3():
    values = path()
    plt.plot(values[0], values[1], 'ro--')
    plt.title('User-Entered Path')
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.grid(True)
    plt.show()



run_task3()