from RedGradient import RedGradient
from GreenGradient import GreenGradient
from BlueGradient import BlueGradient

class GradientFactory():
    def __init__(self):
        pass
    def makeGradient(self, gradientName, iterations):
        if gradientName == None:
            return RedGradient(iterations)
        if gradientName == 'red':
            return RedGradient(iterations)
        elif gradientName == 'blue':
            return BlueGradient(iterations)
        elif gradientName == "green":
            return GreenGradient(iterations)
        else:
            raise NotImplementedError("Invalid gradient requested.")



