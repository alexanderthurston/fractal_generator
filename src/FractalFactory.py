from Fractal import Fractal

class FractalFactory():
    def __init__(self):
        self.__configDict = {}
        pass

    def makeFractal(self, fileName):
        if fileName == None:
            self.__configDict = {
                'type': 'mandelbrot',
                'pixels': 640,
                'centerx': 0.0,
                'centery': 0.0,
                'axislength': 4.0,
                'iterations': 100
            }
        else:
            self.__readFile(fileName)

    def __readFile(self, fileName):

        file = open(fileName)
        for line in file:
            if "#" in line:
                break
            fractalList = line.replace("\n", "").replace(" ", "").split(":")

            if fractalList[0].lower() == "type":
                if fractalList[1].lower() == 'mandelbrot' or fractalList[1].lower() == "julia" or fractalList[1].lower() == "mandelbrot4":
                    self.__configDict[fractalList[0].lower()] = fractalList[1]
            if fractalList[0].lower() == "pixels" and fractalList[1].isdigit():
                self.__configDict[fractalList[0].lower()] = int(fractalList[1])
            if fractalList[0].lower() == "centerx" or fractalList[0].lower() == "centery" or fractalList[0].lower() == "axislength":
                self.__configDict[fractalList[0].lower()] = float(fractalList[1])
            else:
                raise NotImplementedError("Incorrect format in fractal configuration file") #not gonna work but will do for now.

