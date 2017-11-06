from moduleTasks import *
from pprint import pprint as pp

def loadMultiple(signalNames, folderName, maxCount):
    ans = {}
    for item in signalNames:
        try:
            t = loadDataFrom(item, folderName)
            if t[1] > maxCount:
                ans[item] = []
            else:
                ans[item] = t[0]
        except:
            ans[item] = None

    return ans

def saveData(signalsDictionary, targetFolder, bounds, threshold):

    for key, value in signalsDictionary.items():

        if value != None and value != []:
            if (isBounded(value, bounds, threshold) == True):
                ws = str(value[0])
                for item in value:
                    plus = "{0:.3f}".format(float(item))
                    ws = ws + '\n' + plus
                with open('{0}/{1}.txt'.format(targetFolder, key), 'w') as myFile:
                    myFile.writelines(ws)






if "__main__" == __name__:

    d = (loadMultiple(['AFW-481','CIG-308','NIK-876'],'Signals',10))
    saveData(d,'Test',(-12,15),19)

