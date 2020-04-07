""" Creates a Tk window and a  PhotoImage  object; the
PhotoImage  stores the pixels and is capable of creating a PNG image file"""

from tkinter import Tk, Canvas, PhotoImage, mainloop
from GradientFactory import GradientFactory
from colour import Color

class ImagePainter:
    def __init__(self, fractal, gradientName):
        self.__fractal = fractal
        self.__iterations = self.__fractal.getDictVal('iterations')
        self.__gradient = GradientFactory().makeGradient(gradientName, self.__iterations)
        self.__window = Tk()
        self.__width = self.__fractal.getDictVal('pixels')
        self.__height = self.__fractal.getDictVal('pixels')
        self.__color = '#ffffff'
        self.__photoImage = PhotoImage(width=self.__width, height=self.__height)
        self.__paint(self.__fractal)

        # Save the image as a PNG
        self.__photoImage.write(f"{self.__fractal.getDictVal('type')}.png")
        print(f"Wrote image {self.__fractal.getDictVal('type')}.png")

        # Call tkinter.mainloop so the GUI remains open
        mainloop()



    def __paint(self, fractal):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        This code creates an image which is 640x640 pixels in size."""


        minx = fractal.getDictVal('centerx') - (fractal.getDictVal('axislength') / 2.0)
        maxx = fractal.getDictVal('centerx') + (fractal.getDictVal('axislength') / 2.0)
        miny = fractal.getDictVal('centery') - (fractal.getDictVal('axislength') / 2.0)
        pixelsize = abs(maxx - minx) / self.__width


        # Display the image on the screen
        canvas = Canvas(self.__window, width=self.__width, height=self.__height, bg=self.__color)
        canvas.pack()
        canvas.create_image((self.__width / 2, self.__height / 2), image=self.__photoImage, state="normal")

        for row in range(self.__height, 0, -1):
            for col in range(self.__width):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                color = self.__gradient.getColor(self.__fractal.count(complex(x, y)))
                self.__photoImage.put(color, (col, self.__height - row))
            self.__window.update()  # display a row of pixels


