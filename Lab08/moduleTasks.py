import glob
import re
from exModule import runNetworkCode
from pprint import pprint as pp

def checkNetwork(**kwargs):
    try:
        runNetworkCode()
    except ConnectionError as e:
        raise ConnectionError(*e.args)
    except OSError as e:
        return "An issue encountered during runtime. The name of the error is: {}".format(e.__class__.__name__)
    except Exception as e:
        return False
    return True

def isOK(signalName):
    expr = r"[A-Z]{3}\-\d{3}"
    m = re.match(expr,signalName)
    if m is None:
        return False
    return True

def loadDataFrom(signalName, folderName):
    l = []
    no_float = 0
    a = isOK(signalName)
    if a is False:
        raise ValueError(" {} is invalid.".format(signalName))
    found = glob.glob("./{}/{}.txt".format(folderName,signalName))

    if found == []:
        raise OSError("{}.txt is not there in folder {}".format(signalName,folderName))

    with open(found[0], 'r') as File:
        lines = File.readlines()
    for line in lines:
        expr = r"(\-?\d+\.\d+)"
        m = re.match(expr,line)
        if m is None:
            no_float += 1
        else:
            l.append(float(m.group(0)))

    ans = []
    ans.append(l)
    ans.append(no_float)
    t = tuple(ans)

    return t

def isBounded(signalValues, bounds, threshold):
    mnum = 0
    if signalValues == []:
        raise ValueError ("Signal contains no data.")
    for item in signalValues:
        if float(item) < float(bounds[0]) or float(item) > float(bounds[1]):
            mnum += 1
    if mnum > threshold:
        return False
    return True





if "__main__" == __name__:

    (checkNetwork())
    (isOK('AZE-909'))
    pp(loadDataFrom('AFW-481','Signals'))
    (isBounded([2.2,2.4,3,3.5],(2.4,3),2))

