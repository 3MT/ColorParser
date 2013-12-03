
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
