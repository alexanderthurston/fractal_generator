"""The driver program; imports other modules, accepts
command-line arguments and calls upon other modules to display a fractal
on-screen and write a PNG image.  This file is the main entry point of the
program."""
import sys
from FractalFactory import FractalFactory
from ImagePainter import ImagePainter

if __name__ == '__main__':
    if len(sys.argv) < 2:

        ImagePainter(FractalFactory().makeFractal(None), None)

    elif len(sys.argv) < 3:

        ImagePainter(FractalFactory().makeFractal(sys.argv[1]), None)

    else:
        ImagePainter(FractalFactory().makeFractal(sys.argv[1]), sys.argv[2])
