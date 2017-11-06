from simpleVector import *

def loadVectors(filename):
    ans = []
    with open(filename, 'r') as File:
        lines = File.readlines()
    for line in lines:
        try:
            val = Vector(line)
            ans.append(val)
        except:
            ans.append(None)
    return (ans)

if "__main__" == __name__:

    print(loadVectors('values.txt'))