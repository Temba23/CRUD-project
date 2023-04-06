from estd_connection import estd_connection


def update(id, to_change, value):
    cursor = estd_connection()
    sql = f"""
    UPDATE STUDENT SET {to_change.upper()}='{value}' WHERE ID='{id}'
    """
    cursor.execute(sql)
    cont = input("The student has been updated. Do you want to continue? (y/n)")
    return cont.lower() == 'y'


# import json
# filename = "students.json"
# def update(id, to_change, value):
#     # read the students from file
#     # filter the student using id
#     # change the student data using to_change and value
#     # write the student data
#     # continue or not
#     with open(filename, "r") as fp:
#         students = json.load(fp)
#         student = list(filter(lambda x: x['id'] == id, students))
#     student = student[0]
#     index_of_student = students.index(student)
#
#     students[index_of_student][to_change] = [value]
#     with open(filename, 'w') as fp:
#         json.dump(students, fp, indent=2)
#     cont = input("Student has been updated. Do you want to continue? (y/n)")
#     return True if cont.lower() == "y" else False
