1. Requirements:
    Julia Code Smells:

        1. Use of global variables on lines 18 & 19 of src/julia_fractal.py:
            '''
            global grad
            global win
            '''

            Simplified by:
            Reorganizing modules to only use local variables

        2. Use of "magic numbers" on lines 22,28,29, unnecessary assignment to variable on line 26, and index out of range on line 29 of src/julia_fractal.py:

            '''
            for i in range(78):
                z = z * z + c
                if abs(z) > 2:
                    return grad[i]
                     z += z + c
            return grad[77]
            return grad[78]
           '''

           Simplified to:
           '''
            for i in range(len(grad)):
                z = z * z + c
                if abs(z) > 2:
                    return grad[i]

            return grad[len(grad) - 1]
           '''

        3. Unnecessary looping and overuse of conditionals in lines 41-45 of src/julia_fractal.py:
            '''
            for key in dictionary:
                if key in dictionary:
                    if key == name:
                        value = dictionary[key]
                        return key
            '''

            Simplified to:

            '''
            if name in dictionary:
                return name
            '''

        6. Unnecessary formal parameters on line 48, Use of global variables on lines 52-54 and line 64,
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
            '''
            def makePicture(f):
                widthOrHeight = 512

                min = ((f['centerX'] - (f['axisLength'] / 2.0)),
                       (f['centerY'] - (f['axisLength'] / 2.0)))

                max = ((f['centerX'] + (f['axisLength'] / 2.0)),
                       (f['centerY'] + (f['axisLength'] / 2.0)))

                canvas = Canvas(win, widthOrHeight, widthOrHeight, bg="#ffffff")
                canvas.pack()
                canvas.create_image((256, 256), image=photo, state="normal")

                size = abs(max[0] - min[0]) / widthOrHeight

            '''

        7. Confusing variable name and use of "magic numbers" on line 89-94 of src.julia_fractal.py:
            '''
            for r in range(512, 0, -1):
                for c in range(512):
                    x = min[0] + c * size
                    y = min[1] + r * size
                    color = getColorFromGradient(complex(x, y))
                    photo.put(c2, (c, 512 - r))
                win.update()  # display a row of pixels
            '''

            Simplified to:
            '''
            for row in range(512, 0, -1):
                for col in range(512):
                    x = min[0] + col * size
                    y = min[1] + row * size
                    color = getColorFromGradient(complex(x, y))
                    photo.put(color, (col, 512 - row))
                win.update()  # display a row of pixels
            '''

        8. Unnecessary check on line 169 of src/julia_fractal.py:
            '''
            i = getFractalConfigurationDataFromFractalRepositoryDictionary(juliaConfigDict, sys.argv[1])
            '''

            Simplified to:
            '''
            i = sys.argv[1]
            '''

        9. Repetitive code on line 181 of src/julia_fractal.py:
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
           '''
            def colorOfThePixel(c, gradient):
                z = complex(0, 0)  # z0
                MAX_ITERATIONS = len(gradient)
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
            Reorganizing code into modules to eliminate global variables.

        5. Extraneous variables on lines 65,76,77 in src/mbrot_fractal.py:
            '''
            maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

            portion = int(512 / 64)
            total_pixels = 1048576
            '''
            Simplified by:
            Deletion of above code
    Shared Code Smells:
        Both fractal files have various global variables that need to be eliminated as well as a confusing overall structure.
        Code will be split into modules:
            Main.py - Retrieves and verifies user input, then directs information to other modules in program.
            Config.py - Contains fractal configuration dictionaries for other modules to call upon.
            Mandelbrot.py - Returns iteration count for certain point on complex plane for mandelbrot functions.
            Julia.py - Return iteration count for certain point on complex plane for Julia function.
            Gradient.py - contains an array of different color codes corresponding to certain iteration counts.
            ImagePainter.py - Creates a Tk window and PhotoImage object capable of creating a PNG file.










