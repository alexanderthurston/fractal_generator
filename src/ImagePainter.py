""" Creates a Tk window and a  PhotoImage  object; the
PhotoImage  stores the pixels and is capable of creating a PNG image file"""

from tkinter import Tk, Canvas, PhotoImage, mainloop
import Mandelbrot

class ImagePainter:
    def __init__(self, image):

    # Set up the GUI so that we can paint the fractal image on the screen
        self.window = Tk()
        self.img = PhotoImage(width=512, height=512)
        self.paint(Mandelbrot.Mandelbrot.getImage(image))

        # Save the image as a PNG
        self.img.write(f"{image}.png")
        print(f"Wrote image {image}.png")

        # Call tkinter.mainloop so the GUI remains open
        mainloop()

    def colorOfThePixel(self, c, gradient):
        """Return the color of the current pixel within the Mandelbrot set"""
        global z
        z = complex(0, 0)  # z0

        global MAX_ITERATIONS
        global i

        for i in range(MAX_ITERATIONS):
            z = z * z + c  # Get z1, z2, ...
            if abs(z) > 2:
                z = 2.0
                return gradient[i]  # The sequence is unbounded
        # XXX: one of these return statements made the program crash...
        return gradient[MAX_ITERATIONS - 1]


    def paint(self, fractals, imagename):
        """Paint a Fractal image into the TKinter PhotoImage canvas.
        This code creates an image which is 640x640 pixels in size."""



        fractal = fractals[imagename]

        # Figure out how the boundaries of the PhotoImage relate to coordinates on
        # the imaginary plane.
        minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
        maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
        miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
        maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

        # Display the image on the screen
        canvas = Canvas(self.window, width=512, height=512, bg='#ffffff')
        canvas.pack()
        canvas.create_image((256, 256), image=img, state="normal")

        # At this scale, how much length and height on the imaginary plane does one
        # pixel take?
        pixelsize = abs(maxx - minx) / 512

        portion = int(512 / 64)
        total_pixels = 1048576
        for row in range(512, 0, -1):
            for col in range(512):
                x = minx + col * pixelsize
                y = miny + row * pixelsize
                color = colorOfThePixel(complex(x, y), gradient)
                img.put(color, (col, 512 - row))
            window.update()  # display a row of pixels


