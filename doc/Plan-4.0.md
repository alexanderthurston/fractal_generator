1. Requirements:
    Shared Code Smells:
        Both fractal files have various global variables that need to be eliminated as well as a confusing overall structure.
        Code will be split into modules:
            Main.py - Retrieves and verifies user input, then directs information to other modules in program.
            Config.py - Contains fractal configuration dictionaries for other modules to call upon.
            Mandelbrot.py - Returns iteration count for certain point on complex plane for mandelbrot functions.
            Julia.py - Return iteration count for certain point on complex plane for Julia function.
            Gradient.py - contains an array of different color codes corresponding to certain iteration counts.
            ImagePainter.py - Creates a Tk window and PhotoImage object capable of creating a PNG file.

        Standalone array gradient(mbrot_fractal lines 10-27)/grad(julia_fractal lines 99-116) and dictionary
            images(mbrot_fractal lines 99-135)/f(julia_fractal lines 128-147):

            Simplified by:
            Reorganizing modules and storing grad/gradient array in Gradient class. Manipulated juliaGradient to match
                original capabilities of program.
            Reorganizing modules and storing shared dictionary images/f in Config class.

    Julia Code Smells:

        1. Use of global variables on lines 18 & 19, use of "magic numbers" on lines 22,28,29, unnecessary assignment
            to variable on line 26, and index out of range on line 29 of src/julia_fractal.py:
            '''
            global grad
            global win

            for i in range(78):
                z = z * z + c
                if abs(z) > 2:
                    return grad[i]
                     z += z + c
            return grad[77]
            return grad[78]
            '''

            Simplified to:
            Reorganizing grad variable into Gradient class and deletion of win as it is not used in the function.
            '''
            class Julia:

                def __init__(self):
                    self.complexNum = complex(-1.0,0.0)
                    self.gradient = Gradient()

                def pixelColor(self, z):
                    """Return the index of the color of the current pixel within the Julia set
                    in the gradient array"""

                    MAX_ITERATIONS = self.gradient.getLength()

                    for i in range(MAX_ITERATIONS):
                        z = z * z + self.complexNum
                        if abs(z) > 2:
                            return self.gradient.getColor(i)
                    return self.gradient.getColor(MAX_ITERATIONS - 1)
            '''

        2. Unnecessary looping and overuse of conditionals in lines 41-45 of src/julia_fractal.py:
            '''
            for key in dictionary:
                if key in dictionary:
                    if key == name:
                        value = dictionary[key]
                        return key
            '''

            Simplified by:
            Reorganization of check into Config class method containsImage(). Main will check if image is defined by using this method.
            '''
            def containsImage(self, key):
                if key in self.mandelbrotConfigDict or key in self.juliaConfigDict:
                    return True
            '''


        3. Unnecessary formal parameters on line 48, use of global variables on lines 52-54 and line 64,
           unnecessary repetition of method on lines 72,73,74,78,83, irrelevant variables on lines 76,84, and
           use of "magic numbers" on line 81 of src/julia_fractal.py:
            '''
            def makePicture(f, i, e):

                global win
                global grad
                global photo


                min = ((f['centerX'] - (f['axisLength'] / 2.0)),
                       (f['centerY'] - (f['axisLength'] / 2.0)))

                max = ((f['centerX'] + (f['axisLength'] / 2.0)),
                       (f['centerY'] + (f['axisLength'] / 2.0)))

                global WHITE

                canvas = Canvas(win, width=512, height=512, bg=WHITE)
                canvas.pack()
                canvas.create_image((256, 256), image=photo, state="normal")
                canvas.pack()
                canvas.pack()
                canvas.pack()

                area_in_pixels = 512 * 512

                canvas.pack()
                size = abs(max[0] - min[0]) / 512.0

                canvas.pack()
                fraction = int(512/64)

            '''

            Simplified to:
            Reorganization of drawing method from julia_fractal and mbrot_fractal into one cohesive drawing method in ImagePainter class.

            '''
            def paint(self, fractal):

                minx = fractal['centerX'] - (fractal['axisLen'] / 2.0)
                maxx = fractal['centerX'] + (fractal['axisLen'] / 2.0)
                miny = fractal['centerY'] - (fractal['axisLen'] / 2.0)
                pixelsize = abs(maxx - minx) / 512


                canvas = Canvas(self.window, width=self.width, height=self.height, bg=self.color)
                canvas.pack()
                canvas.create_image((256, 256), image=self.photoImage, state="normal")

                for row in range(self.height, 0, -1):
                    for col in range(self.width):
                        x = minx + col * pixelsize
                        y = miny + row * pixelsize
                        if fractal['type'] == 'mandelbrot':
                            color = Mandelbrot().pixelColor(complex(x, y))
                        if fractal['type'] == 'julia':
                            color = Julia().pixelColor(complex(x, y))
                        self.photoImage.put(color, (col, self.height - row))
                    self.window.update()

            '''

        4. Unnecessary check and assignment on line 169 of src/julia_fractal.py:
            '''
            i = getFractalConfigurationDataFromFractalRepositoryDictionary(juliaConfigDict, sys.argv[1])
            '''

            Simplified to:
            Did not perform check or assign value to variable. Passed original variable in as actual parameter to ImagePainter class.
            '''
            ImagePainter(sys.argv[1])
            '''

        5. Repetitive code on line 181 of src/julia_fractal.py:
            '''
            photo.write(i + ".png")
            print("Wrote picture " + i + ".png")
            photo.write(i + ".png")
            '''

            Simplified to:
            '''
            photo.write(i + ".png")
            print("Wrote picture " + i + ".png")
            '''

    Mandelbrot Code Smells:

        1. Unnecessary variable assignment outside of function on lines 29-39 of src/mbrot_fractal.py:
           '''
            MAX_ITERATIONS = len(gradient)
            z = 0


            def colorOfThePixel(c, gradient):
                global z
                z = complex(0, 0)  # z0

                global MAX_ITERATIONS
                global i
           '''
           Simplified to:
           Restructured to function into Mandelbrot class to simplify capabilities and make it easier to understand.
           '''
           class Mandelbrot:

                def __init__(self):
                    self.complexNum = complex(0.0,0.0)

                def pixelColor(self, c):
                    """Return the color of the current pixel within the Mandelbrot set"""

                    MAX_ITERATIONS = Gradient().getLength()
           '''

        2. Unnecessary variable assignment after usage on line 44 of src/mbrot_fractal.py:
            '''
            z = 2.0
            '''
            Simplified by:
            Deletion of above code

        3. Index out of range on line 48 of src/mbrot_fractal.py:
            '''
            return gradient[MAX_ITERATIONS]
            '''
            Simplified by:
            Deletion of above code

        4.  Unnecessary specification within function and use of global variables on line 51,55,56 of src/mbrot_fractal.py:
            '''
            def paint(fractals, imagename):
                global gradient
                global img

                fractal = fractals[imagename]
            '''
            Simplified to:
            '''
            def paint(fractal):
            '''
            Reorganizing code into modules to eliminate global variables as is documented in Julia Code Smells #3.

        5. Extraneous variables on lines 65,76,77 in src/mbrot_fractal.py:
            '''
            maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

            portion = int(512 / 64)
            total_pixels = 1048576
            '''
            Simplified by:
            Deletion of above code

        6. Unused function on line 87-90 of src/mbrot_fractal.py:
            '''
            def pixelsWrittenSoFar(rows, cols):
                pixels = rows * cols
                print(f"{pixels} pixels have been output so far")
                return pixels
            '''
            Simplified by:
            Deletion of above code as it is not used anywhere else in the program.

2. System Analysis - NA

3. System Design -
    Let User Input:
        Fractal selection
    System will:
        Verify selection
        If valid:
            Generate ImagePainter object
            Call on Config class to retrieve fractal data pertinent to fractal drawing.
            Call on Mandelbrot or Julia classes depending on type of fractal selection and retrieve color of current pixel.
                Mandelbrot and Julia classes will call upon gradient class to retrieve color code info.
            Display and update Tkinter window pixel by pixel until completion of drawing.
            Exit when window is closed by user.
        If invalid:
            Print error message
            Print menu selection
            Exit
    Display:
        Pixel by pixel generation of selected fractal.
        Display fractal until user closes window.

4. Implementation - src folder
5. Testing
    Unit Tests-
        All passed.

    All fractal selections result in identical match in output to original code.









