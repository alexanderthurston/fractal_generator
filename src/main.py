"""The driver program; imports other modules, accepts
command-line arguments and calls upon other modules to display a fractal
on-screen and write a PNG image.  This file is the main entry point of the
program."""
import sys
from FractalFactory import FractalFactory
from GradientFactory import GradientFactory
from ImagePainter import ImagePainter

if __name__ == '__main__':
    if len(sys.argv) < 2:

        ImagePainter(FractalFactory().makeFractal(None), GradientFactory())

    elif len(sys.argv) < 3:

        ImagePainter(FractalFactory().makeFractal(sys.argv[1]), GradientFactory())

    else:
        ImagePainter(FractalFactory().makeFractal(sys.argv[1]), GradientFactory().makeGradient(sys.argv[2]))
