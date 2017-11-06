import re
from pprint import pprint as pp

def parseXML(xmlNode):
    l = []
    expr = r"(?P<aname>[a-z]+)=\"(?P<pname>[\w+\s*\w*]+)\"\s"
    m = re.findall(expr,xmlNode)
    return (sorted(m))

def captureNumbers(sentence):
    expr = r"(?:\+?\-?\d+\.\d+e?E?\-?\+?\d*)|(?:\+?\-?\d+)"
    m = re.findall(expr,sentence)
    return (m)

if __name__ == "__main__":
    st = '<person name="Irene Adler" gender="female" age="35" />'
    (parseXML(st))
    sentence = "With the electron's charge being -1.6022e-19, some choices you have are -110, -32.0 and +55.Assume that pi equals 3.1415, 'e' equals 2.7 and Na is +6.0221E+023."
    (captureNumbers(sentence))

