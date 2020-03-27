"""Given a coordinate in the complex plane, return the
iteration count of the Mandelbrot function for that point"""

class Mandelbrot:

    def __init__(self, max_iterations):
        self.__complexNum = complex(0.0, 0.0)
        self.__max_iterations = max_iterations


    def iterationCount(self, c):
        """Return the color of the current pixel within the Mandelbrot set"""

        for i in range(self.__max_iterations):
            self.__complexNum = self.__complexNum * self.__complexNum + c
            if abs(self.__complexNum) > 2:
                return i
        return self.__max_iterations - 1
