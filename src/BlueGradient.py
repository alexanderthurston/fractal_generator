from Gradient import Gradient
from colour import Color

class BlueGradient(Gradient):
    def __init__(self, iterations):
        self.__iterations = iterations
        self.__blue = Color('blue')
        self.__black = Color('black')
        self.__gradient = list(self.__blue.range_to(self.__black, self.__iterations))

    def getColor(self, index):
        return self.__gradient[index]