class Vector:

    def __init__(self,inp):
        l = inp.split(' ')
        self.x = float(l[0])
        self.y = float(l[1])


if "__main__" == __name__:

    a = '0.12 3.14'
    val = Vector(a)
    print (val.x)
    print (val.y)
