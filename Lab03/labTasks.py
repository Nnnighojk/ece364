#! /usr/bin/envpython3.4

def getTotal(accounts):
    ans = []
    for item in accounts:
        name = item.split(':')[0]
        num = item.split(':')[1]
        #print (name)
        #print (num)
        #numl = list(num)
        ad = 0
        num1 = num.split(' ')
        for i in num1:
            if i is not '':
                el1 = i.split('$')[1]
                #print (el1)
                ad += float(el1)
        ans.append(round(ad,2))
    return (ans)

def convertTobinary(num):
    if num == 0: return [0]
    bit = []
    while num:
        bit.append(num % 2)
        num >>= 1
    arr =  bit[::-1]
    return (arr)

def getDoublePalindromes():
    fans = []
    lbin = []

    for item in range(10,1000001):
        lb = list(bin(item))
        for a in range(2,len(lb)):
            lbin.append(lb[a])
        lnum = list(str(item))
        lnew2 = list(reversed(lbin))
        lnew1 = list(reversed(lnum))
        #("".join(lnew1)+" "+"".join(lnum)+" "+str(lnew1==lnum))
        if (lnew1==lnum) and (lnew2==lbin):
            fans.append(item)
        #print("".join(lnew2)+" "+"".join(lbin)+" "+str(lnew2==lbin))
        lbin = []
    return (fans)



if __name__ == "__main__":
    getTotal(["George Teal: $1.00 $2.00 $3.00 $4.01","Christine Doyle: $10.51 $22.49 $12.00 $5.33 $100.00"])
    convertTobinary(10)
    print(getDoublePalindromes())
