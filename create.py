import os
import json
filename = "students.txt"
def create():
    id = input("Enter the id of the student :")
    name = input("Enter the name of the student :")
    dept = input("Enter the department of the student :")

    student = dict(id=id, name=name, department=dept)
    if os.path.exists(filename):
        with open(filename, "r") as fp:
            students = fp.read()
            students = json.loads(students)
    else:
        students = []
    students.append(student)
    with open("students.txt", "w") as fp:
        json.dump(students, fp)
    cont = input("A new student has been added. Do you want to continue? (y/n)")
    return True if cont.lower() == "y" else False
