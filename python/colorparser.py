
        # Color Parser 0.0
        # Creator - Aidan Lee
        # Contact - Aidanl03@gmail.com
        # This code falls under the GNU license

from color import *;
import nltk;

    #RGB values for a lot of different colors.
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
    ["ocean",   0.3, 0.8, 0.8],
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

    #saturation adjectives increase or decrease saturation
    #to do this we multiply the each RGB value by the number associated with the word.
saturationAdjectives = [
    ["vibrant", 1.3],
    ["sharp", 1.3],
    ["dull", 0.7],
    ["sparkly", 1.4],
    ["shiny", 1.4],
    ["matte", 0.7],
    ["cool", 0.9] ]

    #brightness adjectives increase or decrease brightness, they add or subtract equally to each color, increasing brightness but losing some saturation.
brightnessAdjectives = [
    ["bright", 0.3],
    ["light", 0.2],
    ["dim", -0.2],
    ["matte", 0.2],
    ["dark", -0.3] ]
        
    # display color suggestions. Intakes text, compares it to the color list then returns a color it feels is appropriate.
def parseText(text):
    text = text.lower(); #lower case it to avoid issues with capitalisation
    sentence = nltk.word_tokenize(text);  #split the input into a list of words for processing.
    red = 0.0;
    blue = 0.0;
    green = 0.0;
    colorfound = 0;
        #find if any of our words match a color
    for word in sentence:
        for bcolor in baseColors: 
            if word == bcolor[0]:
                colorfound += 1;
                if (colorfound > 1): #if multiple colors match, we sorta average between them.
                    red = (red+bcolor[1])/colorfound;
                    green = (green+bcolor[2])/colorfound;
                    blue = (blue+bcolor[3])/colorfound;
                else:
                    red = bcolor[1];
                    green = bcolor[2];
                    blue = bcolor[3];
                
        #if any words match a brightness word    
    for word in sentence:
        for adj in brightnessAdjectives:
            if word == adj[0]:
                red = max(min(red+adj[1], 1.0), 0.0) #clamp between 0.0 and 1.0
                green = max(min(green+adj[1], 1.0), 0.0)
                blue = max(min(blue+adj[1], 1.0), 0.0)
                
        #if any words match a saturation word...
    for word in sentence:
        for adj in saturationAdjectives:
            if word == adj[0]: 
                red = max(min(red*adj[1], 1.0), 0.0) #clamp between 0.0 and 1.0
                green = max(min(green*adj[1], 1.0), 0.0)
                blue = max(min(blue*adj[1], 1.0), 0.0)
                

    if (colorfound == 0):
        raise NameError('ColorNotFound');
                
    return color(red, green, blue);
