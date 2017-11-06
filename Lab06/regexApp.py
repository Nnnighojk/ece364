import re
from uuid import UUID
from pprint import pprint as pp

def getUrlParts(url):
    expr = r"//(?P<website>www.[\w.-]+)/(?P<two>[\w.-]+)/(?P<three>[\w.-]+)\?"
    m = re.search(expr,url,re.I)
    return ((m.group('website')),(m.group('two')),(m.group('three')))

def getQueryParameters(url):
    expr = r"\?(?P<r11>[\w.-_]+)\=(?P<r12>[\w.-_]+)\&(?P<r21>[\w.-_]+)\=(?P<r22>[\w.-_]+)\&(?P<r31>[\w.-_]+)\=(?P<r32>[\w.-_]+)"
    m = re.search(expr,url,re.I)
    return ([(m.group('r11'),m.group('r12')),(m.group('r21'),m.group('r22')),(m.group('r31'),m.group('r32'))])

def getSpecial(sentence, letter):
    ans = []
    expr1 = r"\b({0}\w*)\b".format(letter)
    expr2 = r"\b(\w*{0})\b".format(letter)
    a =  (re.findall(expr1,sentence,re.I))
    b = re.findall(expr2,sentence,re.I)
    for item in a:
        if item not in b:
            ans.append(item)
    for j in b:
        if j not in a:
            ans.append(j)
    return (ans)

def getRealMAC(sentence):
    expr = r"([a-zA-Z0-9]){2}(:|-)([a-zA-Z0-9]){2}(:|-)([a-zA-Z0-9]){2}(:|-)([a-zA-Z0-9]){2}(:|-)([a-zA-Z0-9]){2}(:|-)([a-zA-Z0-9]){2}"
    m = re.search(expr,sentence)
    return (m.group(0))

def openFile(filename):
    with open(filename, 'r') as File:
        lines = File.readlines()
    return lines

def getName(name):
    expr1 = r"(?P<last>\w+),\s(?P<first>\w+)"
    expr2 = r"(?P<first>\w+)\s(?P<last>\w+)"
    m1 = re.match(expr1,name)
    m2 = re.match(expr2,name)
    if m1:
        return ("{0} {1}".format(m1.group('first'),m1.group('last')))
    if m2:
        return ("{0} {1}".format(m2.group('first'),m2.group('last')))

def getRejectedEntries():
    ans = []
    line  = openFile("Employees.txt")
    for item in line:
        expr = r"(?P<name>\w+,?\s\w+)(?P<data>[,;\s]*)$"
        m = re.match(expr,item,re.I)
        if m is not None:
            ans.append(getName(m.group('name')))
    return (sorted(ans))

def getEmployeesWithIDs():
    ans = {}
    line  = openFile("Employees.txt")
    for item in line:
        expr1 = r"(?P<name>\w+,?\s\w+)(?P<data>[,;\s]*)"
        expr2 = r"({\w+-\w+-\w+-\w+-\w+}|\w+-\w+-\w+-\w+-\w+|\w{32})"
        m1 = re.search(expr1,item)
        m2 = re.search(expr2,item)
        if m1 is not None and m2 is not None:
            ans[getName(m1.group('name'))] = str(UUID(m2.group(1)))
    return (ans)

def getEmployeesWithoutIDs():
    ans = []
    l2 = []
    l1 = getRejectedEntries()
    l = getEmployeesWithIDs()
    for key in l.keys():
        l2.append(key)
    line  = openFile("Employees.txt")
    for item in line:
        expr1 = r"(?P<name>\w+,?\s\w+)(?P<data>[,;\s]*)"
        m1 = re.search(expr1,item)
        if m1 is not None:
            nm = getName(m1.group('name'))
        if nm not in l1 and nm not in l2:
            ans.append(nm)
    return (sorted(ans))

def getPhone(phone):
    l = list(phone)
    expr1 = r"\((?P<first>\d{3})\)\s(?P<two>\d{3})-(?P<three>\d{4})"
    expr2 = r"(?P<first>\d{3})-(?P<two>\d{3})-(?P<three>\d{4})"
    expr3 = r"(\d{10})"
    m1 = re.search(expr1,phone)
    m2 = re.search(expr2,phone)
    m3 = re.search(expr3,phone)
    if m1 is not None:
        return phone
    if m2 is not None:
        return ('('+m2.group('first')+')'+' '+m2.group('two')+'-'+m2.group('three'))
    if m3 is not None:
        return ('('+str(l[0])+str(l[1])+str(l[2])+')'+' '+str(l[3])+str(l[4])+str(l[5])+'-'+str(l[6])+str(l[7])+str(l[8])+str(l[9]))

def getEmployeesWithPhones():
    ans = {}
    line  = openFile("Employees.txt")
    for item in line:
        expr1 = r"(?P<name>\w+,?\s\w+)(?P<data>[,;\s]*)"
        expr2 = r"(\(\d{3}\)\s\d{3}-\d{4}|\d{10}|\d{3}-\d{3}-\d{4})"
        m1 = re.search(expr1,item)
        m2 = re.search(expr2,item)
        if m1 is not None and m2 is not None:
            ans[getName(m1.group('name'))] = getPhone(m2.group(1))
    return (ans)

def getEmployeesWithStates():
    ans = {}
    line  = openFile("Employees.txt")
    for item in line:
        expr1 = r"(?P<name>\w+,?\s\w+)(?P<data>[,;\s]*)"
        expr2 = r"([a-zA-Z]+\s[a-zA-Z]+|[a-zA-Z]+)$"
        m1 = re.search(expr1,item)
        m2 = re.search(expr2,item)
        if m1 is not None and m2 is not None:
            ans[getName(m1.group('name'))] = m2.group(1)
    return (ans)

def getCompleteEntries():
    ans = {}
    id = getEmployeesWithIDs()
    state = getEmployeesWithStates()
    phone = getEmployeesWithPhones()
    line  = openFile("Employees.txt")
    for item in line:
        expr1 = r"(?P<name>\w+,?\s\w+)(?P<data>[,;\s]*)"
        m1 = re.search(expr1,item)
        if getName(m1.group('name')) in id.keys() and getName(m1.group('name')) in state.keys() and getName(m1.group('name')) in phone.keys():
            ans[getName(m1.group('name'))] = (id[getName(m1.group('name'))], phone[getName(m1.group('name'))], state[getName(m1.group('name'))])
    return ans




if __name__ == "__main__":
    url = "http://www.google.com/Math/Const?Pi=3.14&Max_Int=65536&What_Else=Not-Here"
    (getUrlParts(url))
    (getQueryParameters(url))
    s = "The TART program runs on Tuesdays and Thursdays, but it does not start until next week."
    getSpecial(s,"t")
    (getRealMAC("hello hi baby 58:1C:0A:6E:39:4D"))
    (getRejectedEntries())
    (getEmployeesWithIDs())
    (getEmployeesWithoutIDs())
    (getEmployeesWithPhones())
    (getEmployeesWithStates())
    (getCompleteEntries())

