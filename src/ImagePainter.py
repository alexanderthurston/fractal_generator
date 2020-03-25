""" Creates a Tk window and a  PhotoImage  object; the
PhotoImage  stores the pixels and is capable of creating a PNG image file"""

from tkinter import Tk, Canvas, PhotoImage, mainloop
from Config import Config
from Mandelbrot import Mandelbrot
from Julia import Julia

class ImagePainter:
    def __init__(self, image):
        self.__image = image
        self.__window = Tk()
        self.__width = 512
        self.__height = 512
        self.__color = '#ffffff'
        self.__photoImage = PhotoImage(width=self.__width, height=self.__height)
        self.__paint(Config().getImage(self.__image))

        # Save the image as a PNG
        self.__photoImage.write(f"{self.__image}.png")
        print(f"Wrote image {self.__image}.png")

        # Call tkinter.mainloop so the GUI remains open
        mainloop()



    def __paint(self, fractal):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        This code creates an image which is 640x640 pixels in size."""


        minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
        maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
        miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
        pixelsize = abs(maxx - minx) / self.__width


        # Display the image on the screen
        canvas = Canvas(self.__window, width=self.__width, height=self.__height, bg=self.__color)
        canvas.pack()
        canvas.create_image((self.__width / 2, self.__height / 2), image=self.__photoImage, state="normal")

        for row in range(self.__height, 0, -1):
            for col in range(self.__width):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                if fractal['type'] == 'mandelbrot':
                    color = Mandelbrot().pixelColor(complex(x, y))
                if fractal['type'] == 'julia':
                    color = Julia().pixelColor(complex(x, y))
                self.__photoImage.put(color, (col, self.__height - row))
            self.__window.update()  # display a row of pixels


