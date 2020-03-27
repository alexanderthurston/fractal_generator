"""Given a coordinate in the complex plane, return the iteration
count of the Julia function for that point"""

class Julia:

    def __init__(self, max_iterations):
        self.__complexNum = complex(-1.0, 0.0)
        self.__max_iterations = max_iterations

    def iterationCount(self, z):
        """Return the index of the color of the current pixel within the Julia set
        in the gradient array"""



        for i in range(self.__max_iterations): #Customer was not using full gradient of colors in earlier model. Decided to manipulate gradient to keep original capability.
            z = z * z + self.__complexNum
            if abs(z) > 2:
                return i
        return self.__max_iterations - 1

