import matplotlib.pyplot as plt

def small():
    x = [3, 10, 10, 3]
    y = [3, 3, 10, 10]
    plt.plot(x,y)
    plt.show()

def medium():
    x = [2 ,5 ,5 ,2 ,2]
    y = [2 ,2 ,5 ,5 ,2]
    plt.plot(x ,y, 'gs--')
    plt.show()


def large():
    pass

small()
medium()
