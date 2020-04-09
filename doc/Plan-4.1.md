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
        Use Fractal abstract class to call upon subclasses to retrieve iteration count for fractal.
            Subclasses = Mandelbrot, Julia, Mandelbrot4
        Use FractalFactory class to create fractal object from information provided in fractal file.
            If no fractal is specified FractalFactory creates default fractal object.
            If fractal does not exist, open() function fails.
            If file contains errors, throw RuntimeError.
        Use Gradient class to retrieve color of pixel in relation to the iteration count.
        Use GradientFactory class to create user specified gradients

4. Implementation - src folder excluding Testing and Assn4.0 Outdated Files directories

5. Testing - 
    Ran each fractal with different gradient configurations. Expected outcome was observed with each trial. All tests passed.