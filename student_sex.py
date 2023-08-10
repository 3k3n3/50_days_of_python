"""
You work for a school and your boss wants to know how many 
female and male students are enrolled in the school. The school
has saved the students in a list. Your task is to write a code that 
will count how many males and females are in the list.
"""


def student_sex(students: list) -> list:
    students = [x.lower() for x in students]
    sex = set(students)
    list_of_tuple = []
    for i in sex:
        list_of_tuple.append((i, students.count(i)))

    return list_of_tuple


students = [
    "Male",
    "Female",
    "female",
    "male",
    "male",
    "male",
    "female",
    "male",
    "Female",
    "Male",
    "Female",
    "Male",
    "female",
]

print(student_sex(students=students))
