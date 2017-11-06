import glob
from pprint import pprint as pp

def getRegistration():
    cdict = {}
    adict = {}
    lname = []
    files = glob.glob("Classes/*")
    #print (files)
    for item in files:
        with open(item , 'r') as myFile:
            line=myFile.readlines()
            for i in line:
                inew = i.strip()
                if inew not in lname:
                    lname.append(inew)
    for b in lname:
        cdict[b] = set()
    for item in files:
        with open(item , 'r') as myFile:
            line=myFile.readlines()
            for i in line:
                inew = i.strip()
                for a in lname:
                    if a == inew:
                        fname = item.split('/')[1]
                        fn = fname.split('.')[0]
                        cdict[inew].add(fn)
    for key,value in cdict.items():
        adict[key] = sorted(value)
    return (adict)

def getCommonClasses(studentName1,studentName2):
    cdict={}
    valid1 = 0
    valid2 = 0
    lans = []
    l1 = []
    l2 = []
    cdict = getRegistration()
    for key, value in cdict.items():
        if key == studentName1:
            l1 = value
            valid1 = 1
        if key == studentName2:
            l2 = value
            valid2 = 0
    if valid2 == 0 or valid1 == 0:
        return (None)
    for a in l1:
        for b in l2:
            if a == b:
                lans.append(a)

    return (set(lans))



if __name__ == "__main__":
    getRegistration()
    getCommonClasses("Tasha Shell","Tamatha Granderson")