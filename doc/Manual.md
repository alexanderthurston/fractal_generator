Hello and Welcome to the Fractals Program User Manual!

Please initialize the program by using a set of instructions from an option below:
    
    If you would like for our program to generate a default fractal for you, simply run the main.py file using it's 
    relative path on your computer from the command line. Ex. "python src/main.py"
    
    If you would like to specify a particular fractal from the list below, please run the main.py file using it's 
    relative path on your computer with the addition of the file path and name as a second argument. 
      Ex. "python src/main.py data/funnel-down.frac"
        Fractal options include:
            branches.frac
            branches256.frac
            connected.frac
            elephant.frac
            elephants.frac
            fulljulia.frac
            fullmandelbrot.frac
            funnel-down.frac
            hourglass.frac
            lakes.frac
            leaf.frac
            mandelfour.frac
            mandelfull.frac
            minibrot.frac
            seahorse.frac
            spiral0.frac
            spiral1.frac
            spiral-jetty.frac
            unconnected.frac
            wholly-squid.frac
            zoomed.frac
    
    If you would like to specify both the fractal and gradient please run the main.py file from it's relative path on 
    your computer with the addition of the fractal file name and the name of the gradient.
      Ex. "python src/main.py data/fullmandelbrot.frac blue"
        Gradient options include:
            red
            green
            blue
            
    Unfortunately, with our system configuration it is not possible to specify the gradient without specifying the fractal,
    but we'll get it on the next update! Thank you for your continued support!
   
    Depending on your previous selection, a fractal will begin drawing in a separate window, but be cautious, if the window is closed before the
    drawing is completed it will not save the drawing and will result in a program error. If this occurs simply rerun
    the last command and wait for the drawing to complete.

That's it! Please enjoy the full set of fractal options at your disposal.
