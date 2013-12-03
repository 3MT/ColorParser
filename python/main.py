
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
        ["red",         "Color(1.0, 0.0, 0.0)"],
        ["RED",         "Color(1.0, 0.0, 0.0)"],
        ["Red",         "Color(1.0, 0.0, 0.0)"],
        ["rEd",         "Color(1.0, 0.0, 0.0)"],
        ["asdfa red",   "Color(1.0, 0.0, 0.0)"],
        ["asdfadsfred", "Error"],
        ["blue",        "Color(1.0, 0.0, 0.0)"],
        ["green",       "Color(1.0, 0.0, 0.0)"],
        ["cyan",        "Color(1.0, 0.0, 0.0)"],
        ["teal",        "Color(1.0, 0.0, 0.0)"],
        ["yellow",      "Color(1.0, 0.0, 0.0)"],
        ["purple",      "Color(1.0, 0.0, 0.0)"],
        ["pink",        "Color(1.0, 0.0, 0.0)"],
        ["bright red",  "Color(1.0, 0.0, 0.0)"],
        ["dark red",    "Color(1.0, 0.0, 0.0)"],
        ["dim red",     "Color(1.0, 0.0, 0.0)"],
        ["light red",   "Color(1.0, 0.0, 0.0)"],
        ["black",       "Color(1.0, 0.0, 0.0)"],
        ["white",       "Color(1.0, 0.0, 0.0)"],
        ["magenta",     "Color(1.0, 0.0, 0.0)"],
        ["brown",       "Color(1.0, 0.0, 0.0)"] ]
    for test in tests:
        print ''
        print 'Input: {0}'.format(test[0]);
        print 'Expected Output:'
        print '{0}'.format(test[1]);
        print 'Actual Output: '
        parseText(test[0]).printColor();
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
        if color_raw == "test":
            testColors();
        red = color(1.0,0.0,0.0);
        red.printColor();
