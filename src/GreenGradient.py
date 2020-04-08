from Gradient import Gradient
from colour import Color

class GreenGradient(Gradient):
    def __init__(self, iterations):
        self.__iterations = iterations
        self.__green = Color('green')
        self.__black = Color('black')
        self.__gradient = list(self.__green.range_to(self.__black, self.__iterations))

    def getColor(self, index):
        return str(self.__gradient[index].get_hex_l())