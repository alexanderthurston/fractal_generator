from Gradient import Gradient
from colour import Color
class RedGradient(Gradient):

    def __init__(self, iterations):
        self.__iterations = iterations
        self.__red = Color('red')
        self.__black = Color('black')
        self.__gradient = list(self.__red.range_to(self.__black, self.__iterations))


    def getColor(self, index):
        return str(self.__gradient[index].get_hex_l())