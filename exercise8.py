import numpy as np
import matplotlib.pyplot as plt

def extract():
    a = np.arange(16)
    print(a)
    b = a.reshape(4,4)
    print("The output of b is")
    print(b)
    c = b[1:3, 1:4]
    print("The shape of c is", c.shape)
    print("The output of c is")
    print(c)

def graph():
    x = np.linspace(-2, 2, 200)
    y = x**2+10
    plt.title("Quadratic function")
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")
    plt.plot(x,y,label="curve")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    extract()
    graph()