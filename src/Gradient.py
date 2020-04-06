class Gradient:
    def __init__(self):
        raise NotImplementedError("Concrete subclass of Gradient must implement __init__")

    def getColor(self, index):
        raise NotImplementedError("Concrete subclass of Gradient must implement getColor() method")
