""" Creates a Tk window and a  PhotoImage  object; the
PhotoImage  stores the pixels and is capable of creating a PNG image file"""

from tkinter import Tk, Canvas, PhotoImage, mainloop

class ImagePainter:
    def __init__(self, fractal, gradient, configDict):
        self.__configDict = configDict
        self.__fractal = fractal
        self.__gradient = gradient
        self.__window = Tk()
        self.__width = self.__configDict['pixels']
        self.__height = self.__configDict['pixels']
        self.__bgColor = '#ffffff'
        self.__photoImage = PhotoImage(width=self.__width, height=self.__height)
        self.__paint()

        # Save the image as a PNG
        self.__photoImage.write(f"{self.__configDict['type']}.png")
        print(f"Wrote image {self.__configDict['type']}.png")

        # Call tkinter.mainloop so the GUI remains open
        mainloop()



    def __paint(self):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        This code creates an image which is 640x640 pixels in size."""


        minx = self.__configDict['centerx'] - (self.__configDict['axislength'] / 2.0)
        maxx = self.__configDict['centerx'] + (self.__configDict['axislength'] / 2.0)
        miny = self.__configDict['centery'] - (self.__configDict['axislength'] / 2.0)
        pixelsize = abs(maxx - minx) / self.__width


        # Display the image on the screen
        canvas = Canvas(self.__window, width=self.__width, height=self.__height, bg=self.__bgColor)
        canvas.pack()
        canvas.create_image((self.__width / 2, self.__height / 2), image=self.__photoImage, state="normal")

        for row in range(self.__height, 0, -1):
            for col in range(self.__width):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                count = self.__fractal.count(complex(x, y))
                color = self.__gradient.getColor(count)
                self.__photoImage.put(color, (col, self.__height - row))
            self.__window.update()  # display a row of pixels

