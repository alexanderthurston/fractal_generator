"""Contains a Python dictionary composed of fractal
configuration data"""

"""Extract the contents of these dictionaries from the starter programs and unite
them in one dictionary in the Config.py module.  To distinguish Julia
fractals from Mandelbrot fractals add a new key/value pair to each dictionary:"""

class Config:
    def __init__(self):

        self.__mandelbrotConfigDict = {
                'fullmandelbrot': {
                    'type': 'mandelbrot',
                    'c': complex(0.0, 0.0),
                    'centerX': -0.6,
                    'centerY': 0.0,
                    'axisLen': 2.5,
                    },

                'spiral0': {
                    'type': 'mandelbrot',
                    'c': complex(0.0, 0.0),
                    'centerX': -0.761335372924805,
                    'centerY': 0.0835704803466797,
                    'axisLen': 0.004978179931102462,
                    },

                'spiral1': {
                    'type': 'mandelbrot',
                    'c': complex(0.0, 0.0),
                    'centerX': -0.747,
                    'centerY': 0.1075,
                    'axisLen': 0.002,
                    },

                'seahorse': {
                    'type': 'mandelbrot',
                    'c': complex(0.0, 0.0),
                    'centerX': -0.745,
                    'centerY': 0.105,
                    'axisLen': 0.01,
                    },

                'elephants': {
                    'type': 'mandelbrot',
                    'c': complex(0.0, 0.0),
                    'centerX':  0.30820836067024604,
                    'centerY':  0.030620936230004017,
                    'axisLen':  0.03,
                    },

                'leaf': {
                    'type': 'mandelbrot',
                    'c': complex(0.0, 0.0),
                    'centerX': -1.543577002,
                    'centerY': -0.000058690069,
                    'axisLen':  0.000051248888,
                    },
                }

        self.__juliaConfigDict = {
            'fulljulia': {
                'type': 'julia',
                'c': complex(-1.0, 0.0),
                'centerX': 0.0,
                'centerY': 0.0,
                'axisLen': 4.0,
            },

            'hourglass': {
                'type': 'julia',
                'c': complex(-1.0, 0.0),
                'centerX': 0.618,
                'centerY': 0.00,
                'axisLen': 0.017148277367054,
            },

            'lakes': {
                'type': 'julia',
                'c': complex(-1.0, 0.0),
                'centerX': -0.339230468501458,
                'centerY': 0.417970758224314,
                'axisLen': 0.164938488846612,
            },

        }

    def containsImage(self, key):
        if key in self.__mandelbrotConfigDict or key in self.__juliaConfigDict:
            return True

    def getImage(self, key):
        if key in self.__mandelbrotConfigDict:
            return self.__mandelbrotConfigDict[key]
        if key in self.__juliaConfigDict:
            return self.__juliaConfigDict[key]

    def printAll(self):
        print("\nMandelbrot Fractals")
        for i in self.__mandelbrotConfigDict:
            print(f"\t{i}")
        print("\nJulia Fractals")
        for i in self.__juliaConfigDict:
            print(f"\t{i}")