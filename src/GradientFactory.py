from RedGradient import RedGradient
from GreenGradient import GreenGradient
from BlueGradient import BlueGradient

class GradientFactory():
    def __init__(self):
        pass
    def makeGradient(self, configDict, gradientName):
        if gradientName == None:
            return RedGradient(configDict['iterations'])
        if gradientName == 'red':
            return RedGradient(configDict['iterations'])
        elif gradientName == 'blue':
            return BlueGradient(configDict['iterations'])
        elif gradientName == "green":
            return GreenGradient(configDict['iterations'])
        else:
            raise NotImplementedError("Invalid gradient requested.")



