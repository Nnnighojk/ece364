

class Rectangle:

    def __init__(self, llPoint, urPoint):
        if type(llPoint) != tuple or type(urPoint) != tuple:
            raise TypeError ("Wrong type!!")
        if llPoint[0] >= urPoint[0] or llPoint[1] >= urPoint[1]:
            raise ValueError("Lower-Left point must be less than Upper-Right point. ")
        self.lowerLeft = llPoint
        self.upperRight = urPoint

    def isSquare(self):
        if self.upperRight[0] - self.lowerLeft[0] == self.upperRight[1] - self.lowerLeft[1]:
            return True
        return False

    def isPointInside (self,other):
        valid1 = 0
        valid2 = 0
        if type(other) != tuple:
            raise TypeError ("Wrong type!!")
        if self.lowerLeft[0] < other[0] and other[0] < self.upperRight[0]:
            valid1 = 1
        if self.lowerLeft[1] < other[1] and other[1] < self.upperRight[1]:
            valid2 = 1
        if valid1 == 1 and valid2 == 1:
            return True
        return False


    def intersectsWith(self, rect):
        p1 = (rect.lowerLeft[0],rect.upperRight[1])
        p2 = (rect.upperRight[0],rect.lowerLeft[1])
        if self.isPointInside(rect.upperRight) == True or self.isPointInside(rect.lowerLeft) == True or self.isPointInside(p1) == True or self.isPointInside(p2) == True:
            return True
        return False


if "__main__" == __name__:

    a = Rectangle((1,1),(3,3))
    val = a.isSquare()
    val2 = a.isPointInside((2,2))
    c = Rectangle((2,2),(4,4))
    b = a.intersectsWith(c)
    print (b)

