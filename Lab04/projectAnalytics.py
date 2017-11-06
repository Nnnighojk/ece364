#! /usr/bin/envpython3.4
from pprint import pprint as pp

def getComponentCountByProject(projectID):
    lv = []
    li = []
    r = 0
    l = 0
    c = 0
    t = 0
    valid = 0
    l1 = []
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for item in line[2:]:
            k = item.split(' ')[14].strip()
            v = item.split(' ')[5].strip()
            if k == projectID:
                lv.append(v)
                valid = 1
    if valid == 0:
        return None
    for item in lv:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            for i in line[4:]:
                el = i.split(",")
                for j1 in el:
                    nj1 = j1.strip()
                    if nj1 not in l1:
                        l1.append(nj1)
    # j = list(l)
    #pp (l)
    for item in l1:
        j = list(item)
        if j[0] == "R" or j[1] == "R":
            r += 1
        if j[0] == "L" or j[1] == "L":
            l += 1
        if j[0] == "C" or j[1] == "C":
            c += 1
        if j[0] == "T" or j[1] == "T":
            t += 1
    li.append(r)
    li.append(l)
    li.append(c)
    li.append(t)
    t = tuple(li)
    return (t)

def getComponentCountByStudent(studentName):
    clist = []
    li = []
    r = 0
    l = 0
    c = 0
    t = 0
    valid = 0
    nid = 0
    lnew = []
    with open('students.txt', 'r') as myFile:
        line=myFile.readlines()
        for item in line[2:]:
            name = item.split("|")
            na = name[0].strip()
            if na == studentName:
                nid = name[1].strip()
                valid = 1
    if valid == 0:
        return None
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for item in line[2:]:
            val = item.split(' ')[5]
            if val not in clist:
                clist.append(val)
    for item in clist:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            numid = (line[1]).split(",")
            for a in numid:
                if nid == a.strip():
                    con = (line[4]).split(",")
                    for b in con:
                        bnew = b.strip()
                        if bnew not in lnew:
                            lnew.append(bnew)
    for item in lnew:
        j = list(item)
        if j[0] == "R" or j[1] == "R":
            r += 1
        if j[0] == "L" or j[1] == "L":
            l += 1
        if j[0] == "C" or j[1] == "C":
            c += 1
        if j[0] == "T" or j[1] == "T":
            t += 1
    li.append(r)
    li.append(l)
    li.append(c)
    li.append(t)
    t = tuple(li)
    return (t)

def getParticipationByStudent(studentName):
    clist = []
    l = []
    ans = []
    nid = 0
    valid = 0
    with open('students.txt', 'r') as myFile:
        line=myFile.readlines()
        for j in line[2:]:
            name = j.split("|")
            na = name[0].strip()
            if na == studentName:
                nid = name[1].strip()
                valid = 1
    if valid == 0:
        return None
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            val = i.split(' ')[5]
            if val not in clist:
                clist.append(val)
    for item in clist:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            numid = (line[1]).split(",")
            for a in numid:
                if nid == a.strip():
                    l.append(item)
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            val = i.split(' ')[5]
            fid = i.split(' ')[14].strip()
            for z in l:
                if z == val:
                    ans.append(fid)
    return (set(ans))

def getParticipationByProject(projectID):
    clist = []
    lname1 = []
    lname2 = []
    ans = []
    valid = 0
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            val = i.split(' ')[14].strip()
            vid = i.split(' ')[5].strip()
            if val == projectID:
                clist.append(vid)
                valid = 1
    if valid == 0:
        return None
    for item in clist:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            numid = (line[1]).split(",")
            for a in numid:
                lname1.append(a.strip())
    for b in lname1:
        if b not in lname2:
            lname2.append(b)
    with open('students.txt', 'r') as myFile:
        line=myFile.readlines()
        for j in line[2:]:
            name = j.split("|")
            na = name[0].strip()
            idnum = name[1].strip()
            for c in lname2:
                if c == idnum:
                    ans.append(na)
    return (set(ans))

def getProjectByComponent(components):
    cdict = {}
    adict = {}
    compare = sorted(components)
    for i in compare:
        cdict[i]= set()
    for f in compare:
        adict[f] = set()
    clist = []
    lans = []
    ans = []
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            val = i.split(' ')[5]
            if val not in clist:
                clist.append(val)
    for item in clist:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            comp = (line[4]).split(",")
            for u in compare:
                for w in comp:
                    wnew = w.strip()
                    if u == wnew:
                        cdict[u].add(item)
    #print (cdict)
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            cir = i.split(' ')[5] #circuit id
            cid = i.split(' ')[14] #project id
            cnew = cid.strip() #project id
            #for item in compare: #list of components
            for key,value in cdict.items():
                if cir in value: #set of circuit ids
                   # print('d = ', d, 'cir = ', cir)
                    adict[key].add(cnew)
    return (adict)

def getStudentByComponent(components):
    complis = sorted(components)
    cdict = {}
    adict = {}
    for i in complis:
        cdict[i]= set()
        adict[i] = set()
    clist = []
    nname = []
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            val = i.split(' ')[5]
            if val not in clist:
                clist.append(val)
    for item in clist:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            comp = (line[4]).split(",")
            sname = (line[1]).split(",")
            for i in sname:
                nname.append(i.strip())
            for u in complis:
                for w in comp:
                    wnew = w.strip()
                    if wnew == u:
                        for g in nname:
                            cdict[u].add(g)
            nname = []
    #pp (cdict)
    with open('students.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            cir = i.split('|') #circuit id
            name = cir[0].strip()
            sid = cir[1].strip()
            for key,value in cdict.items():
                if sid in value:
                    adict[key].add(name)
    return (adict)

def getComponentByStudent(studentNames):
    nlist = sorted(studentNames)
    ndict = {}
    clist = []
    adict = {}
    comp = []
    for item in nlist:
        adict[item] = set()
    nname = []
    with open('students.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            cir = i.split('|')
            name = cir[0].strip()
            sid = cir[1].strip()
            for item in nlist:
                if item == name:
                    ndict[name] = sid
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            val = i.split(' ')[5].strip()
            if val not in clist:
                clist.append(val)
    for item in clist:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            nomp = (line[4]).split(",")
            for v in nomp:
                comp.append(v.strip())
            scomp =  (set(comp))
            sname = (line[1]).split(",")
            for i in sname:
                nname.append(i.strip())
            #print (nname)
            for key, value in ndict.items():
                if value in nname:
                    adict[key] |= (scomp)
            nname = []
            comp = []
    return (adict)

def getCommonByProject(projectID1, projectID2):
    l1 = []
    l2 = []
    l1c = []
    l2c = []
    ans = []
    valid1 = 0
    valid2 = 0
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            cir = i.split(' ')[5] #circuit id
            cid = i.split(' ')[14] #project id
            cnew = cid.strip() #project id
            if cnew == projectID1:
                l1.append(cir)
                valid1 = 1
            if cnew == projectID2:
                l2.append(cir)
                valid2 = 1
    if valid1 == 0 or valid2 == 0:
        return None
    for item in l1:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            comp = (line[4]).split(",")
            for a in comp:
                l1c.append(a.strip())
    for item in l2:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            comp1 = (line[4]).split(",")
            for b in comp1:
                l2c.append(b.strip())
    ans = set(l1c) & set(l2c)
    return ((sorted(ans)))

def getCommonByStudent(studentName1, studentName2):
    clist = []
    comp = []
    nname = []
    l1 = []
    l2 = []
    valid1 = 0
    valid2 = 0
    a = 0
    b = 0
    with open('students.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            cir = i.split('|')
            name = cir[0].strip()
            sid = cir[1].strip()
            if name == studentName1:
                a = sid
                valid1 = 1
            if name == studentName2:
                b = sid
                valid2 = 1
    if valid1 == 0 or valid2 == 0:
        return None
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            val = i.split(' ')[5].strip()
            if val not in clist:
                clist.append(val)
    for item in clist:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            nomp = (line[4]).split(",")
            for v in nomp:
                comp.append(v.strip())
            sname = (line[1]).split(",")
            for i in sname:
                nname.append(i.strip())
            if a in nname:
                for h in comp:
                    l1.append(h)
            if b in nname:
                for h in comp:
                    l2.append(h)
            comp = []
            nname = []
    ans = set(l1) & set(l2)
    return (sorted(ans))

def getProjectByCircuit():
    clist = []
    l = []
    adict = {}
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            val = i.split(' ')[5].strip()
            if val not in clist:
                clist.append(val)
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            cir = i.split(' ')[5]
            cirn = cir.strip()#circuit id
            cid = i.split(' ')[14] #project id
            cnew = cid.strip() #project id
            for item in clist:
                if item == cirn:
                    l.append(cnew)
            adict[cirn] = sorted(l)
            l = []
    return (adict)

def getCircuitByStudent():
    cdict = {}
    clist = []
    comp = []
    l = []
    adict = {}
    ans = {}
    with open('students.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            cir = i.split('|')
            name = cir[0].strip()
            sid = cir[1].strip()
            cdict[name] = sid
            adict[name] = set()
    with open('projects.txt', 'r') as myFile:
        line=myFile.readlines()
        for i in line[2:]:
            val = i.split(' ')[5].strip()
            if val not in clist:
                clist.append(val)
    for item in clist:
        with open('Circuits/circuit_'+item+'.txt', 'r') as myFile:
            line=myFile.readlines()
            nomp = (line[4]).split(",")
            #for v in nomp:
            #    comp.append(v.strip())
            sname = (line[1]).split(",")
            for key, value in cdict.items():
                for z in sname:
                    if value == z.strip():
                        adict[key].add(item)
    for key, value in adict.items():
        lans = sorted(value)
        ans[key] = lans
    return (ans)

def getCircuitByStudentPartial(studentName):
    cdict = {}
    adict = {}
    cdict = getCircuitByStudent()
    valid = 0
    for key, value in cdict.items():
        k = key.split(',')
        k1 = k[0].strip()
        k2 = k[1].strip()
        if studentName == key or studentName == k1 or studentName == k2:
            adict[key] = value
            valid = 1
    if valid == 0:
        return None
    return (adict)

if __name__ == "__main__":
    (getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6"))
    (getComponentCountByStudent("Adams, Keith"))
    (getParticipationByStudent("Young, Frank"))
    (getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6"))
    getProjectByComponent({'T71.386', 'C407.660', 'L760.824', 'R497.406', 'T77.624', 'T426.533', 'C313.400','R591.569'})
    getStudentByComponent({'T71.386', 'C407.660', 'L760.824', 'R497.406', 'T77.624', 'T426.533', 'C313.400','R591.569'})
    (getComponentByStudent({'Young, Frank', 'Robinson, Pamela', 'White, Diana'}))
    getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", '90BE0D09-1438-414A-A38B-8309A49C02EF')
    getCommonByStudent("Young, Frank", "White, Diana")
    getProjectByCircuit()
    getCircuitByStudent()
    (getCircuitByStudentPartial("James"))
