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

        9. Confusing variable name on line 89,90 of src.julia_fractal.py:
            '''
            c2 = getColorFromGradient(complex(x, y))
            photo.put(c2, (c, 512 - r))
            '''

            Simplified to:
            '''
            color = getColorFromGradient(complex(x, y))
            photo.put(color, (c, 512 - r))
            '''

        10. Unnecessary check on line 169 of src/julia_fractal.py:
            '''
            i = getFractalConfigurationDataFromFractalRepositoryDictionary(juliaConfigDict, sys.argv[1])
            '''

            Simplified to:
            '''
            i = sys.argv[1]
            '''

        11.
            Repetitive code:
            '''
            photo.write(i + ".png")
            print("Wrote picture " + i + ".png")
            photo.write(i + ".png")
            '''

            Simplified by:
            Deletion of second photo.write(i + ".png")

    Mandelbrot Code Smells:

        1.
            Unnecessary variable assignment outside of function:
                MAX_ITERATIONS = len(gradient)
                z = 0
                global i
            Simplified by:
                Defining both variables within the function they're being using in.
        2.
            Unnecessary variable assignment after usage:
                z = 2.0
            Simplified by:
                Deletion of above code
        3.
            Index out of range:
                return gradient[MAX_ITERATIONS]
            Simplified by:
                Deletion of above code
        4.
            Unnecessary specification within function and use of global variables:
                def paint(fractals, imagename):
                    global gradient
                    global img

                    fractal = fractals[imagename]
            Simplified by:
                def paint(fractal): #fractal is specified as parameter before being passed into the method

                Reorganizing modules to only use local variables
        5.
            Extraneous variables:
                maxy = fractal['centerY'] + (fractal['axisLen'] / 2.0)

                portion = int(512 / 64)
                total_pixels = 1048576
            Simplified by:
                Deletion of above code









