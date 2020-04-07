"""Given a coordinate in the complex plane, return the iteration
count of the Julia function for that point"""
from Fractal import Fractal

class Julia(Fractal):

    def __init__(self, configDict):
        self.__configDict = configDict
        self.__complexNum = complex(-1.0, 0.0)
        self.__max_iterations = self.__configDict['type']

    def count(self, z):
        """Return the index of the color of the current pixel within the Julia set
        in the gradient array"""

        for i in range(self.__max_iterations):
            z = z * z + self.__complexNum
            if abs(z) > 2:
                return i
        return self.__max_iterations - 1

    def getDictVal(self, key):
        return self.__configDict[key]

