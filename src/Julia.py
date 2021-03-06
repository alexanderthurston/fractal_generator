"""Given a coordinate in the complex plane, return the iteration
count of the Julia function for that point"""
from Fractal import Fractal

class Julia(Fractal):

    def __init__(self, iterations):

        self.__complexNum = complex(-1.0, 0.0)
        self.__max_iterations = iterations

    def count(self, z):
        """Return the index of the color of the current pixel within the Julia set
        in the gradient array"""
        comp = self.__complexNum
        for i in range(self.__max_iterations):
            z = z * z + comp
            if abs(z) > 2:
                return i
        return self.__max_iterations - 1


