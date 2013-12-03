
        # Color Parser 0.0
        # Creator - Aidan Lee
        # Contact - Aidanl03@gmail.com
        # This code falls under the GNU license

from color import *;
from colorparser import *;

    # test function (tests a bunch of predefined strings)
def testColors():
    # test cases, left is input and right is roughly the expected output.
    tests = [
        ["red",         "Color(0.7, 0.0, 0.0)"],
        ["RED",         "Color(0.7, 0.0, 0.0)"],
        ["Red",         "Color(0.7, 0.0, 0.0)"],
        ["rEd",         "Color(0.7, 0.0, 0.0)"],
        ["asdfa red",   "Color(0.7, 0.0, 0.0)"],
        ["asdfadsfred", "Error"],
        ["blue",        "Color(0.0, 0.0, 0.7)"],
        ["green",       "Color(0.0, 0.7, 0.0)"],
        ["cyan",        "Color(0.0, 0.9, 0.9)"],
        ["teal",        "Color(0.0, 0.7, 0.7)"],
        ["yellow",      "Color(1.0, 1.0, 0.0)"],
        ["purple",      "Color(0.7, 0.0, 0.7)"],
        ["pink",        "Color(1.0, 0.4, 0.4)"],
        ["bright red",  "Color(1.0, 0.1, 0.1)"],
        ["dark red",    "Color(0.5, 0.0, 0.0)"],
        ["dim red",     "Color(0.6, 0.0, 0.0)"],
        ["light red",   "Color(1.0, 0.2, 0.2)"],
        ["black",       "Color(0.0, 0.0, 0.0)"],
        ["white",       "Color(0.0, 0.0, 0.0)"],
        ["magenta",     "Color(0.8, 0.0, 0.6)"],
        ["brown",       "Color(0.4, 0.3, 0.2)"] ]
    for test in tests:
        print ''
        print 'Input: {0}'.format(test[0]);
        print 'Expected Output:'
        print '{0}'.format(test[1]);
        print 'Actual Output: '
        try:
            parseText(test[0]).printColor();
        except NameError:
            print 'Error: No matching color';


        
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
        elif color_raw == "test":
            testColors();
        else:
            try:
                c = parseText(color_raw);
                c.printColor();
            except NameError:
                print 'Sorry, none of that was recognised as a color.';
