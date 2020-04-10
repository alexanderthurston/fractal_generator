"""Contains a Python dictionary composed of fractal
configuration data"""

"""Extract the contents of these dictionaries from the starter programs and unite
them in one dictionary in the Config.py module.  To distinguish Julia
fractals from Mandelbrot fractals add a new key/value pair to each dictionary:"""

class Config:
    def __init__(self):
        self.__configDict = {}
        pass

    def readFile(self, fileName):
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
            self.__configDict = {}
            temp_dict = {}
            checkList = ['type', 'pixels', 'centerx', 'centery', 'axislength', 'iterations']

            file = open(fileName)
            for line in file:
                if line.startswith("#") or line.endswith(":"):
                    continue
                else:
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
                else:
                    raise NotImplementedError("Incorrect format in fractal configuration file")

        return self.__configDict


