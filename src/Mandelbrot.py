"""Given a coordinate in the complex plane, return the
iteration count of the Mandelbrot function for that point"""
from Gradient import Gradient
class Mandelbrot:

    def pixelColor(self, c):
        """Return the color of the current pixel within the Mandelbrot set"""
        z = complex(0, 0)  # z0
        MAX_ITERATIONS = Gradient().getLength()

        for i in range(MAX_ITERATIONS):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                return Gradient().getColor(i)  # The sequence is unbounded
        # XXX: one of these return statements made the program crash...
        return Gradient().getColor(MAX_ITERATIONS - 1)

