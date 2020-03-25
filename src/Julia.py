"""Given a coordinate in the complex plane, return the iteration
count of the Julia function for that point"""
from Gradient import Gradient
class Julia:

    def __init__(self):
        self.complexNum = complex(-1.0,0.0)
        self.gradient = Gradient()

    def pixelColor(self, z):
        """Return the index of the color of the current pixel within the Julia set
        in the gradient array"""

        MAX_ITERATIONS = self.gradient.getLength()

        for i in range(MAX_ITERATIONS): #Customer was not using full gradient of colors in earlier model. Decided to use full gradient instead.
            z = z * z + self.complexNum #If customer is not satisfied I can easily fix the coloration by reverting to the original code or manipulating gradient array.
            if abs(z) > 2:
                return self.gradient.getColor(i)
        return self.gradient.getColor(MAX_ITERATIONS - 1)

