__author__ = 'Araja Jyothi Babu'

def createEmployRecord(name, salary, dept, empId):
    employRecord = {"Name": name, "Salary": salary, "Dept": dept, "EmpId": empId }
    return employRecord

def displayEmployRecord(employ):
    for key, value in employ.items():
        print key, ":", value

def test():
    employRecord = createEmployRecord("Jyothi Babu Araja", 52000, "CSE", "12131A0505")
    displayEmployRecord(employRecord)

test()