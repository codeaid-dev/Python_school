import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(lr, noi, left, right, lower, upper):
    n=lr # line resolution
    iteration_number = noi # number of iterations
    M = np.zeros([n,n],int)
    xvalues = np.linspace(left, right, n)    # region spanning -2 to 0.5
    yvalues = np.linspace(lower, upper, n)   # region spanning -1 to 1
    for u, x in enumerate(xvalues):
        for v, y in enumerate(yvalues):
            z = 0 + 0j # initialization
            C = complex(x, y)
            for i in range(iteration_number):
                z = z * z + C
                # the cumulative absolute value of z going to infinity (bound)
                if abs(z) > 2.0:
                    M[v, u] = 1
                    break
    plt.imshow(M, origin="lower", extent=(left, right, lower, upper)) # creating the image with axes label
    plt.gray()  # grayscale image
    plt.show()  # image output

num = input('Which Mandelbrot do you want to show ?: ')
if (int(num) == 1):
    # full Mandelbrot
    mandelbrot(1000, 100, -2.0, 0.5, -1, 1)
elif (int(num) == 2):
    # Sea Horse Valley
    mandelbrot(1000, 100, -0.85, -0.65, 0.025, 0.2)
else:
    # Elephant Valley
    mandelbrot(1000, 100, 0.2, 0.4, -0.1, 0.1)
