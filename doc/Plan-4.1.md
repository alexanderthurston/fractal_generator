1. Requirements -
    User will:
        Run command line prompt including possible specification of fractal file and possible specification of fractal
    System will:
        Use default values for fractal or gradient if no specification is given.
        Throw appropriate errors if program is not utilized correctly.
        Create and reference new gradient
        Display default or specified fractal
        
        
2. System Analysis - NA

3. System Design - 

    User will:
        Run Command line prompt with or without fractal and gradient specifications.
    System will:
        Use Config class to read through file and return a configuration dictionary for other classes to reference.
        Use FractalFactory class to create fractal object from information provided in fractal file.
            If no fractal is specified FractalFactory creates default fractal object.
            If fractal does not exist, open() function fails.
            If file contains errors, throw RuntimeError.
        Use Fractal abstract class to call upon subclasses to retrieve iteration count for fractal.
            Subclasses = Mandelbrot, Julia, Mandelbrot4
        Use GradientFactory class to create user specified gradient
        Use Gradient class to retrieve color of pixel in relation to the iteration count.
        Use ImagePainter class to compile all information and display fractal line by line until completion.
        

4. Implementation - src folder excluding Testing and Assn4.0 Outdated Files directories

5. Testing - 
    Ran program with no arguments. Defaults executed properly. All tests passed.
    Ran program with fractal argument but no gradient argument. Specified fractal was generated and default gradient was used. All tests passed.
    Ran each fractal with different gradient configurations. Expected outcome was observed with each trial. All tests passed.