#! /usr/bin/envpython3.4

def find(pattern):
    with open('sequence.txt', 'r') as myFile:
        line=myFile.read()
        mas=list(line)
        arr = list(pattern)
        size = len(arr)
        l = []
        for i in range(0,len(mas)):
            if arr[0] == mas[i] or arr[0] is 'X':
                l.append(mas[i:i+size])
        ans = []
        count = 0
        for item in l:
            for i in range(0,len(item)):
                if arr[i] == item[i] or arr[i] is 'X':
                    count += 1
            if count == len(pattern):
                ans.append(item)
            count = 0
        fans = []
        for item in ans:
            fans.append(''.join(item))
        return (fans)

def getStreakProduct(sequence, maxSize, product):
    slist = list(sequence)
    l = []
    for i in range(0,len(slist)):
        for z in range(1,maxSize+1):
            l.append(slist[i:i+z])
    lfin = []
    for item in l:
        if len(item) is not 1 and item not in lfin:
            lfin.append(item)
    prod = 1
    ans = []
    for item in lfin:
        for i in item:
            prod = prod * int(i)
        if prod is product:
            ans.append(item)
        prod = 1
    fans = []
    for item in ans:
        fans.append(''.join(item))
    return (fans)

def writePyramids(filePath, baseSize, count, char):
    with open(filePath,"w+") as fout:
        for i in range(0,int((baseSize+1)/2)):
            for j in range(0,count):
                fout.write(" " * (int((baseSize-1)/2)-i) + char * (2 * i + 1) + " " * (int((baseSize-1)/2)-i))
                if j != count-1:
                    fout.write(' ')
            fout.write('\n')

def getStreaks(sequence, letters):
    s1 = list(sequence)
    l1 = list(letters)
    fans = []
    ans = []
    a = ''
    index = 0
    for item in s1:
        if item in l1:
            if item in a:
                a = a + item
            else:
                if a is not '':
                    ans.append(a)
                a = ''
                a = a + item
        else:
            ans.append(a)
            a = ''
        index = index + 1
        if index == len(s1):
            ans.append(a)
    for item in ans:
        if item is not '':
            fans.append(item)
    return(fans)



def findNames(nameList, part, name):
    f = []
    l = []
    ans = []
    for item in nameList:
        i1 = item.split()[0]
        f.append(i1)
        i2 = item.split()[1]
        l.append(i2)
    if part is "F":
        for i in range(0,len(f)):
            if f[i].lower() == name.lower():
                ans.append(nameList[i])
    if part is "L":
        for i in range(0,len(l)):
            if l[i].lower() == name.lower():
                ans.append(nameList[i])
    if part is "FL":
        for i in range(0,len(nameList)):
            if f[i].lower() == name.lower() or l[i].lower() == name.lower():
                ans.append(nameList[i])
    return (ans)

def convertToBoolean(num, size):
    if num == 0: return [0]
    bit = []
    while num:
        bit.append(num % 2)
        num >>= 1
    arr =  bit[::-1]
    ans = []
    if len(arr) is not size:
        for i in range(0,size-len(arr)):
            ans.append(False)
    for item in arr:
        if item == 1:
            ans.append(True)
        if item == 0:
            ans.append(False)
    return (ans)

def convertToInteger(boolList):
    decimal = 0
    l1 = []
    for item in boolList:
        if item == True:
            l1.append(1)
        if item == False:
            l1.append(0)
    for digit in l1:
        decimal = decimal*2 + int(digit)
    return (decimal)



if __name__ == "__main__":
     (find("9XX3"))
     (getStreakProduct("111111",5,1))
     writePyramids("p1", 13, 6, "X")
     (findNames(["George Smith", "Mark Johnson", "Cordell Theodore", "Maria Satterfield","Johnson Cadence"],"FL","JOHNSON"))
     (convertToBoolean(9,9))
     convertToInteger([False, False, True, False, False, True])
     getStreaks("AAASSSSSSAPPPSSPPBBCCCSSS", "PAZ")