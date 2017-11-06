import re
from enum import Enum
import random

class Level(Enum):
    freshman = 1
    sophomore = 2
    junior = 3
    senior = 4

class Student(object):

    def __init__(self, ID, firstName, lastName, level):
        if type(level) != Level:
            raise TypeError("The argument must be an instance of the ‘Level’ Enum.")
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        self.level = level

    def __str__(self):
        return ("{}, {} {}, {}".format(self.ID, self.firstName, self.lastName, self.level))

def fright(var,let,vname):
        expr = r"{}\d{3}\.\d{3}".format(let)
        for item in var:
            m = re.match(expr,item)
            if m is None:
                raise ValueError("The {}’ list contain invalid components.".format(vname))

class Circuit (object):

    def __init__(self,ID,resistors,capacitors,inductors,transistors):


        fright(resistors, "R", "resistors")
        fright(capacitors, "C", "capacitors")
        fright(inductors, "L", "inductors")
        fright(transistors, "T", "transistors")

        self.ID = ID
        self.resistors = resistors
        self.capacitors = capacitors
        self.inductors = inductors
        self.transistors = transistors

        self.transistors = sorted(self.transistors)
        self.inductors = sorted(self.inductors)
        self.capacitors = sorted(self.capacitors)
        self.resistors = sorted (self.resistors)

    def __str__(self):
        return ("{}: (R = {}, C = {}, L = {}, T = {})".format(self.ID, str(len(self.resistors)).zfill(2), str(len(self.capacitors)).zfill(2),str(len(self.inductors)).zfill(2),str(len(self.transistors)).zfill(2)))

    def getDetails(self):
        ans = self.ID + ":"
        for item in self.resistors:
            ans += " {},".format(item)
        for item in self.capacitors:
            ans += " {},".format(item)
        for item in self.inductors:
            ans += " {},".format(item)
        for item in self.transistors:
            ans += " {},".format(item)

        return ans

    def __contains__(self, item):
        l = ["R", "C", "L", "T"]
        if item[0] not in l:
            raise ValueError("Wrong item value!")
        if type(item) is not str:
            raise TypeError ("Wrong item type!")

        valid = 0
        if item in self.resistors:
            valid = 1
        if item in self.transistors:
            valid = 1
        if item in self.inductors:
            valid = 1
        if item in self.capacitors:
            valid = 1

        if valid == 1:
            return True
        else:
            return False

        def __add__(self, other):
            l = ["R", "T", "L", "C"]
            if type(other) is not Circuit and type(other) is not str:
                raise TypeError ("Wrong other type!")

            if type(other) is str and other[0] not in l:
                raise ValueError ("Wrong value type!")


            if type(other) is str:
                if other[0] is "R":
                    if other in self.resistors:
                        return self
                    self.resistors.append(other)
                    self.resistors = sorted(self.resistors)
                if other[0] is "L":
                    if other in self.inductors:
                        return self
                    self.inductors.append(other)
                    self.inductors = sorted(self.inductors)
                if other[0] is "C":
                    if other in self.capacitors:
                        return self
                    self.capacitors.append(other)
                    self.capacitors = sorted(self.capacitors)
                if other[0] is "T":
                    if other in self.transistors:
                        return self
                    self.transistors.append(other)
                    self.transistors = sorted(self.transistors)
                return self

            if type(other) is Circuit:
                ID = "".join(map(str(random.sample(range(0,9),5))))
                resistor = list(set(self.resistors) | set(other.resistors))
                capacitor = list(set(self.capacitors)|set(other.capacitors))
                inductor = list(set(self.inductors)|set(other.inductors))
                transistor = list(set(self.transistors)|set(other.transistors))
                new_c = Circuit(ID,resistor,capacitor,inductor,transistor)

                return (new_c)

        def __sub__(self, other):
            l = ["R", "T", "L", "C"]
            if type(other) is not str:
                raise TypeError ("Incorrect type!")
            if type(other) is str and other[0] not in l:
                raise ValueError ("Wrong value type!")

            if other[0] == "R":
                if other in self.resistors:
                    self.resistors.remove(other)
            if other[0] == "C":
                if other in self.capacitors:
                    self.capacitors.remove(other)
            if other[0] == "L":
                if other in self.inductors:
                    self.inductors.remove(other)
            if other[0] == "T":
                if other in self.transistors:
                    self.transistors.remove(other)
            return (self)

class Project(object):
    def __init__(self,ID, parti, circuits):
        if type(parti) is not list or parti == []:
            raise ValueError ("Wrong value!")
        for item in parti:
            if type(item) is not Student:
                raise ValueError ("Wrong value!")
        if type(circuits) is not list or circuits == []:
            raise ValueError ("Wrong value!")
        for item in circuits:
            if type(item) is not Circuit:
                raise ValueError ("Wrong value!")
        self.ID = ID
        self.participants = parti
        self.circuits = circuits

    def __str__(self):
        return "{}: {} Circuits, {} Participants".format(self.ID,str(len(self.circuits)).zfill(2),str(len(self.participants)).zfill(2))

    def getDetails(self):
        ans = self.ID + '\n\n'
        ans += "Participants:\n"
        for i in self.participants:
            ans += i.__str__() + '\n'
        ans += '\n'
        ans += "Circuits\n"
        for j in self.circuits:
            ans += j.getDetails() + '\n'
        return ans

    def __contains__(self, item):
        if type(item) != str and type(item) != Circuit and type(item) != Student:
            raise TypeError ("Wrong type!")

        if type(item) == Circuit:
            for i in self.circuits:
                if item.ID == i.ID:
                    return True
                return False
        if type(item) == Student:
            for j in self.participants:
                if item.ID == j.ID:
                    return True
                return False

        if type(item) == str:
            l = ["R", "T", "L", "C"]
            if item[0] not in l:
                raise ValueError ("Wrong Value!")
            for c in self.circuits:
                if item in c:
                    return True
            return False

    def __add__(self, other):
        if type(other) != Circuit and type(other) != Student:
            raise TypeError ("Wrong type!")

        if type(other) == Circuit:
            if not self.__contains__(other):
                self.circuits.append(other)

        if type(other) == Student:
            if not self.__contains__(other):
                self.participants.append(other)

        return self

    def __sub__(self, other):
        if type(other) != Circuit and type(other) != Student:
            raise TypeError ("Wrong type!")

        if type(other) == Circuit:
            for i in self.circuits:
                if (other.ID == i.ID):
                    self.circuits.remove(other)

        if type(other) == Student:
            for j in self.participants:
                if (other.ID == j.ID):
                    self.participants.remove(other)

        return self

class Capstone(Project):
    def __init__(self, ID, parti, circuits):
        for item in parti:
            if item.level != Level.senior:
                raise ValueError ("Wrong value!")
        Project.__init__(self, ID, parti, circuits)

    def __add__(self, other):
        if other.level != Level.senior:
            raise ValueError ("Wrong value!")
        Project.__add__(self,other)





if "__main__" == __name__:
    a = Student("99999-99999","Nivedita","Nighojkar",Level.senior)



