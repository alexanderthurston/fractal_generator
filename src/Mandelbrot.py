"""Given a coordinate in the complex plane, return the
iteration count of the Mandelbrot function for that point"""
from Fractal import Fractal

class Mandelbrot(Fractal):

    def __init__(self, iterations):

        self.__complexNum = complex(0.0, 0.0)
        self.__max_iterations = iterations

    def count(self, c):
        """Return the iteration count of the current pixel within the Mandelbrot set"""
        comp = self.__complexNum
        for i in range(self.__max_iterations):
            comp = comp * comp + c
            if abs(comp) > 2:
                return i
        return self.__max_iterations - 1

