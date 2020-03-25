"""Given a coordinate in the complex plane, return the iteration
count of the Julia function for that point"""
from Gradient import Gradient
class Julia:

    def __init__(self):
        self.__complexNum = complex(-1.0, 0.0)
        self.__gradient = Gradient("julia")

    def pixelColor(self, z):
        """Return the index of the color of the current pixel within the Julia set
        in the gradient array"""

        MAX_ITERATIONS = self.__gradient.getLength()

        for i in range(MAX_ITERATIONS): #Customer was not using full gradient of colors in earlier model. Decided to manipulate gradient to keep original capability.
            z = z * z + self.__complexNum
            if abs(z) > 2:
                return self.__gradient.getColor(i)
        return self.__gradient.getColor(MAX_ITERATIONS - 1)

