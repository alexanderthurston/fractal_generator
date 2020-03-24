""" Creates a Tk window and a  PhotoImage  object; the
PhotoImage  stores the pixels and is capable of creating a PNG image file"""

from tkinter import Tk, Canvas, PhotoImage, mainloop
from Config import Config
from Mandelbrot import Mandelbrot
from Julia import Julia

class ImagePainter:
    def __init__(self, image):
        self.image = image
        self.window = Tk()
        self.width = 512
        self.height = 512
        self.color = '#ffffff'
        self.photoImage = PhotoImage(width=self.width, height=self.height)
        self.paint(Config().getImage(self.image))

        # Save the image as a PNG
        self.photoImage.write(f"{self.image}.png")
        print(f"Wrote image {self.image}.png")

        # Call tkinter.mainloop so the GUI remains open
        mainloop()



    def paint(self, fractal):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        This code creates an image which is 640x640 pixels in size."""


        minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
        maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
        miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
        pixelsize = abs(maxx - minx) / 512


        # Display the image on the screen
        canvas = Canvas(self.window, width=self.width, height=self.height, bg=self.color)
        canvas.pack()
        canvas.create_image((256, 256), image=self.photoImage, state="normal")

        # At this scale, how much length and height on the imaginary plane does one
        # pixel take?

        for row in range(512, 0, -1):
            for col in range(512):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                if fractal['type'] == 'mandelbrot':
                    color = Mandelbrot().pixelColor(complex(x, y))
                if fractal['type'] == 'julia':
                    color = Julia().pixelColor(complex(x, y))
                self.photoImage.put(color, (col, 512 - row))
            self.window.update()  # display a row of pixels


