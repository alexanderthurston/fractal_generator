"""Given a coordinate in the complex plane, return the
iteration count of the Mandelbrot function for that point"""
from Gradient import Gradient
class Mandelbrot:

    def __init__(self):
        self.__complexNum = complex(0.0, 0.0)
        self.__gradient = Gradient()

    def pixelColor(self, c):
        """Return the color of the current pixel within the Mandelbrot set"""

        MAX_ITERATIONS = Gradient().getLength()

        for i in range(MAX_ITERATIONS):
            self.__complexNum = self.__complexNum * self.__complexNum + c
            if abs(self.__complexNum) > 2:
                return self.__gradient.getColor(i)
        return self.__gradient.getColor(MAX_ITERATIONS - 1)
