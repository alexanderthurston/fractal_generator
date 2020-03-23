"""The driver program; imports other modules, accepts
command-line arguments and calls upon other modules to display a fractal
on-screen and write a PNG image.  This file is the main entry point of the
program."""
import sys
from Config import Config

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide the name of a fractal as an argument")
        Config().printAll()
        sys.exit(1)

    elif not Config().containsImage():
        print(f"ERROR: {sys.argv[1]} is not a valid fractal")
        print("Please choose one of the following:")
        Config().printAll()
        sys.exit(1)

    else:
        image = sys.argv[1]
