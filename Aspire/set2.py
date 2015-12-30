__author__ = 'Araja Jyothi Babu'

class Student:
    def __init__(self, name="StudentName", number = "12345", marks=[0,0,0,0,0]):
        self.name = name
        self.number = number
        self.marks = marks
    def totalMarks(self):
        return sum(self.marks)
    def averageMarks(self):
        return sum(self.marks)/len(self.marks)


class ParentAge:
    def setAge(self,age):
        self.age = age
    def getAge(self):
        return self.age

class ChildAge(ParentAge):
    def __init__(self, age):
        self.age = age


def cubes(number):
    return map(lambda x:x**3, range(number))

def test():
    """s1 = Student("Jyothi Babu Araja", "12131A0505", [95,90,92,95,96])
    s2 = Student()
    print s2.name, s2.number, s2.marks
    print s1.name, s1.number, s1.marks
    print s1.totalMarks()
    print s1.averageMarks()"""
    childAge = ChildAge(10)
    print childAge.getAge()
    print cubes(10)
    assert False
