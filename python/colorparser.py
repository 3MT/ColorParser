
        # Color Parser 0.0
        # Creator - Aidan Lee
        # Contact - Aidanl03@gmail.com
        # This code falls under the GNU license

from color import *;

baseColors = [
    ["red",     0.7, 0.0, 0.0],
    ["blue",    0.0, 0.0, 0.7],
    ["green",   0.0, 0.7, 0.0],
    ["orange",  0.7, 0.4, 0.0],
    ["yellow",  0.9, 0.9, 0.0],
    ["purple",  0.7, 0.0, 0.7],
    ["pink",    0.8, 0.4, 0.4],
    ["cyan",    0.0, 0.9, 0.9],
    ["teal",    0.0, 0.6, 0.6],
    ["magenta", 0.8, 0.0, 0.5],
    ["silver",  0.5, 0.5, 0.6],
    ["gold",    0.7, 0.7, 0.0],
    ["brown",   0.4, 0.3, 0.2],
    ["navy",    0.0, 0.0, 0.3],
    ["crimson", 0.3, 0.0, 0.0],
    ["black",   0.0, 0.0, 0.0],
    ["white",   1.0, 1.0, 1.0],
    ["gray",    0.5, 0.5, 0.5],
    ["grey",    0.5, 0.5, 0.5] ]
        
    # display color suggestions. Intakes text, compares it to the color list then returns a color it feels is appropriate.
def parseText(text):
    for bcolor in baseColors:
        if text == bcolor[0]:
            print 'match found...';
            return color(bcolor[1],bcolor[2],bcolor[3]); #returns the first exact match.
    print 'no matches returning black';
    return color(0.0,0.0,0.0);
