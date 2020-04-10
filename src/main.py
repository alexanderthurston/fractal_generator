"""The driver program; imports other modules, accepts
command-line arguments and calls upon other modules to display a fractal
on-screen and write a PNG image.  This file is the main entry point of the
program."""
import sys
from FractalFactory import FractalFactory
from GradientFactory import GradientFactory
from ImagePainter import ImagePainter
from Config import Config

if __name__ == '__main__':

    if len(sys.argv) < 2:
        configDict = Config().readFile(None)
        ImagePainter(FractalFactory().makeFractal(configDict), GradientFactory().makeGradient(configDict, None), configDict)

    elif len(sys.argv) < 3:
        configDict = Config().readFile(sys.argv[1])
        ImagePainter(FractalFactory().makeFractal(configDict), GradientFactory().makeGradient(configDict, None), configDict)

    else:
        configDict = Config().readFile(sys.argv[1])
        ImagePainter(FractalFactory().makeFractal(configDict), GradientFactory().makeGradient(configDict, sys.argv[2]), configDict)
