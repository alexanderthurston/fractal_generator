from Julia import Julia
from Mandelbrot import Mandelbrot
from Mandelbrot4 import Mandelbrot4


class FractalFactory():
    def __init__(self):
        self.__configDict = {}

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
            return Mandelbrot(self.__configDict)
        else:
            self.__configDict = self.__readFile(fileName)
            if self.__configDict['type'] == 'mandelbrot':
                return Mandelbrot(self.__configDict)
            elif self.__configDict['type'] == 'julia':
                return Julia(self.__configDict)
            elif self.__configDict['type'] == 'mandelbrot4':
                return Mandelbrot4(self.__configDict)

    def __readFile(self, fileName):
        self.__configDict = {}
        temp_dict = {}
        checkList = ['type', 'pixels', 'centerx', 'centery', 'axislength', 'iterations']

        file = open(fileName)
        for line in file:
            if "#" in line or line.endswith(":"):
                continue
            fractalList = line.replace("\n", "").replace(" ", "").split(":")

            temp_dict[fractalList[0].lower()] = fractalList[1]

        for i in checkList:
            if i in temp_dict:
                if i == "type":
                    self.__configDict[i] = temp_dict[i]
                elif i == "pixels" or i == "iterations" and temp_dict[i].isdigit():
                    self.__configDict[i] = int(temp_dict[i])
                elif i == "centerx" or i == "centery" or i == "axislength":
                    self.__configDict[i] = float(temp_dict[i])
                # else:
                #     raise NotImplementedError("Incorrect format in fractal configuration file")
            else:
                raise NotImplementedError("Incorrect format in fractal configuration file")

        return self.__configDict

