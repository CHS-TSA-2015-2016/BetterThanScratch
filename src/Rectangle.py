"""
    Generic Rectangle class
    It simply defines a mathematical space, and
    allows for figuring out it's interaction with
    other rectangles [and shapes]
"""
def Rectangle(object):
    """
        function: __init__
        args:
            x=0 ------------ the x-position (in pixels) of the upper left coordinate of the rectangle, defaults at 0;
            y=0 ------------ the y-position (in pixels) of the upper left coordinate of the rectangle, defaults at 0;
            width=1 -------- the width of the rectangle, defaults at 1;
            height=1 ------- the height of the rectangle, defaults at 1;
        purpose:
            basic constructor
    """
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x;
        self.y = y;
        self.width = width;
        self.height = height;

    """
        function: getDimensions
        args:
            none;
        purpose:
            returns a touple (,,,) containing the dimensions of the rectangle:
                (x, y, width, height)
    """
    def getDimensions(self):
        return (self.x, self.y, self.width. self.height);

    """
        function: getPosition
        args:
            none;
        purpose:
            returns a touple (,) containing the position of the upper-left corner of the rectangle
                (x, y)
    """
    def getPosition(self):
        return (self.x, self.y);

    """
        function: getSize
        args:
            none;
        purpose:
            returns a touple (,) containing the size of the window
                (width, height)
    """
    def getSize(self):
        return (self.width, self.height);

    """
        function: setDimensions
        args:
            dimensions ------- a touple (,,,) containing the dimensions of the rectangle (x, y, width, height)
        purpose:
            changing the dimensions of the rectangle
    """
    def setDimensions(self, dimensions):
        self.x, self.y, self.width, self.height = dimensions;

    """
        function: setPosition
        args:
            position --------- a touple (,) containing the position of the upper-lefthand corner of the rectangle (x, y)
        purpose:
            changing the position of the rectangle
    """
    def setPosition(self, position):
        self.x, self.y = position;

    """
        function: setSize
        args:
            size ------------- a touple (,) containing the size of the rectangle (width, height);
        purpose:
            resizing the rectangle
    """
    def setSize(self, size):
        self.width, self.height = size;

    """
        function: copyRectangle
        args:
            rectangle -------- the rectangle object to copy
        purpose:
            repositions and resizes the rectangle to match the given rectangle
    """
    def copyRectangle(self, rectangle):
        self.setDimensions(rectangle.getDimesnions());

    """
        function: copyPosition
        args:
            rectangle -------- the rectangle object to copy
        purpose:
            repositions the rectangle to match the position of the given rectangle
    """
    def copyPosition(self, rectangle):
        self.setPosition(rectangle.getPosition());

    """
        function: copySize
        args:
            rectangle --------- the rectangle object to copy
        purpose:
            resizes the rectangle to match the size of the given rectangle
    """
    def copySize(self, rectangle):
        self.setSize(rectangle.getSize());

    """
        function: pointInSelf
        args:
            point ------------- a touple (,) containing the position of the point to check
        purpose:
            returns True if the point is contained in the rectangle
    """
    def pointInSelf(self, point):
        return (self.x in range(self.x+self.width)) and (self.y in range(self.y+self.height));

    """
        function: rectangleInSelf
        args:
            rectangle --------- the rectangle object to check
        purpose:
            returns True if the given rectangle is completely encased in the calling rectangle
    """
    def rectangleInSelf(self, rectangle):
        rectPos = rectangle.getPosition();
        rectSize = rectangle.getSize();
        point1 = rectPos;
        point2 = (point1(0)+rectSize(0), point(1)+rectSize(1));
        return (self.pointInSelf(point1) and self.pointInSelf(point2));

    """
        function: rectangleIntersectsSelf
        args:
            rectangle ---------- the rectangle object to check
        purpose:
            checks if the given rectangle overlaps the calling rectangle at all
    """
    def rectangleIntersectsSelf(self, rectangle):
        pass;
