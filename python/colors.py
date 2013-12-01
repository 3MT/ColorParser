
        # Color Parser 0.0
        # Creator - Aidan Lee
        # Contact - Aidanl03@gmail.com
        # This code falls under the GNU license

    # simple color class.
class color(object):
    r = 0.0;
    g = 0.0;
    b = 0.0;
    def __init__(self,r,g,b):
        self.r = r;
        self.g = g;
        self.b = b;

    def printColor(self):
        print 'Color({0}, {1}, {2})'.format(self.r,self.g,self.b);
        
    # red color generator
def red(sat,brt):
    pass;

    # orange color generator
def orange(sat,brt):
    pass;
    
    # yellow color generator
def yellow(sat,brt):
    pass;
    
    # green color generator
def green(sat,brt):
    pass;
    
    # cyan color generator
def cyan(sat,brt):
    pass;
    
    # blue color generator
def blue(sat,brt):
    pass;

    # purple color generator
def purple(sat,brt):
    pass;
    
    # pink color generator
def pink(sat,brt):
    pass;
    
    # brown color generator
def brown(sat,brt):
    pass;
    
    # grey color generator
def grey(sat,brt):
    pass;

    # dictionary of function calls to generate colors.
colors = {  1 : red,
            2 : orange,
            3 : yellow,
            4 : green,
            5 : cyan,
            6 : blue,
            7 : purple,
            8 : pink,
            9 : brown,
            10: grey }
        
    # display color suggestions.
    # hue is the color, see the color dictionary
    # saturation is how close to grey it is, 0 is grey, 10 is vivid as possible.
    # brightness is how dark/light, 0 is black, 10 is white, 5 is average.
    # note that this input is not the same as the standardised hue/saturation/brightness system!
def outputColors(hue, saturation, brightness):
    colors[hue]();
        
    # parse text or something

    # main loop.
if __name__ == '__main__':
    end = False;
    print("Welcome to ColorParser 0.0");
    print("Creator - Aidan Lee");
    print("");
    print("Instructions:");
    print("Enter the name of a color and the program will output several hexadecimal colors it thinks match.");
    print("Enter quit at any time to end the program.");
    print("");

    while(not end):
        color_raw = raw_input('Enter name of color:')
        if color_raw == "quit":
            end = True;
        red = color(1.0,0.0,0.0);
        red.printColor();
