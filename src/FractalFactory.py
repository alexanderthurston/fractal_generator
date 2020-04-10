from Julia import Julia
from Mandelbrot import Mandelbrot
from Mandelbrot4 import Mandelbrot4

class FractalFactory():

    def makeFractal(self, configDict):

        if configDict['type'] == 'mandelbrot':
            return Mandelbrot(configDict['iterations'])
        elif configDict['type'] == 'julia':
            return Julia(configDict['iterations'])
        elif configDict['type'] == 'mandelbrot4':
            return Mandelbrot4(configDict['iterations'])



