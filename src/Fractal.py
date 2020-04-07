class Fractal():
    def __init__(self, configDict):
        raise NotImplementedError("Concrete subclass of Fractal must implement __init__")
    def count(self, z):
        raise NotImplementedError("Concrete subclass of Fractal must implement count() method")
    def getDictVal(self):
        pass