from Fractal import Fractal

class Mandelbrot4(Fractal):

    def __init__(self, max_iterations):
        super().__init__()
        self.__complexNum = complex(0.0, 0.0)
        self.__max_iterations = max_iterations

    def count(self, c):
        """Return the color of the current pixel within the Mandelbrot set"""

        for i in range(self.__max_iterations):
            self.__complexNum = (self.__complexNum ** 4) + c
            if abs(self.__complexNum) > 2:
                return i
        return self.__max_iterations - 1