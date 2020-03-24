"""Given a coordinate in the complex plane, return the iteration
count of the Julia function for that point"""
from Gradient import Gradient
class Julia:

    def __init__(self):
        self.complexNum = complex(-1.0,0.0)

    def pixelColor(self, z):
        """Return the index of the color of the current pixel within the Julia set
        in the gradient array"""



        MAX_ITERATIONS = Gradient().getLength()

        for i in range(MAX_ITERATIONS):
            z = z * z + self.complexNum  # Iteratively compute z1, z2, z3 ...
            if abs(z) > 2:
                return Gradient().getColor(i)
        return Gradient().getColor(MAX_ITERATIONS - 1)

