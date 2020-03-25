"""Given a coordinate in the complex plane, return the
iteration count of the Mandelbrot function for that point"""
from Gradient import Gradient
class Mandelbrot:

    def __init__(self):
        self.complexNum = complex(0.0,0.0)

    def pixelColor(self, c):
        """Return the color of the current pixel within the Mandelbrot set"""

        MAX_ITERATIONS = Gradient().getLength()

        for i in range(MAX_ITERATIONS):
            self.complexNum = self.complexNum * self.complexNum + c
            if abs(self.complexNum) > 2:
                return Gradient().getColor(i)
        return Gradient().getColor(MAX_ITERATIONS - 1)
