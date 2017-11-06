from signals import *
import sys
#----------Testing part 1------------------
print("\n\n----------Testing part 1------------------\n\n")
a = loadDataFrom('AFW-481', 'Signals')
b = loadDataFrom('HPQ-298', 'Signals')
c = loadDataFrom('PVL-758', 'Signals')
print("loadDataFrom outputs:")
print( a, '\n\n', b, '\n\n', c)
for i in range(13, 22):
    print("isBounded outputs for range -{} to {}:".format(i, i))
    print(isBounded(a[0], (-1*i, i), 7))
    print(isBounded(b[0], (-1*i, i), 7))
    print(isBounded(c[0], (-1*i, i), 7))
#----------Testing part 2------------------
print("\n\n----------Testing part 2------------------\n\n")
signalsDict = loadMultiple(['AFW-481', 'CIG-308.txt', 'FPT-701', 'GUO-758', 'HPQ-298', 'InvalidNamedSignal','HQP-689', 'ABC-123', 'XZC-901'], 'Signals', 8)
#print(signalsDict)
for (key, values) in signalsDict.items():
    print('signalsDict[{}] = {}\n\n'.format(key, values))
saveData(signalsDict, "target", (-15, 15), 7)

