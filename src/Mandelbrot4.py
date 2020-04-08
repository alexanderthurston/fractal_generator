from Fractal import Fractal

class Mandelbrot4(Fractal):

    def __init__(self, configDict):
        self.__configDict = configDict
        self.__complexNum = complex(0.0, 0.0)
        self.__max_iterations = self.__configDict['iterations']

    def count(self, c):
        """Return the color of the current pixel within the Mandelbrot set"""
        comp = self.__complexNum
        for i in range(self.__max_iterations):
            comp = (comp ** 4) + c
            if abs(comp) > 2:
                return i
        return self.__max_iterations - 1

    def getDictVal(self, key):
        return self.__configDict[key]