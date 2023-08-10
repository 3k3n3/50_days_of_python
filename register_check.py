"""
Write a function called register_check that checks how many 
students are in school. The function takes a dictionary as a 
parameter. If the student is in school, the dictionary says ‘yes’. If 
the student is not in school, the dictionary says ‘no’. Your 
function should return the number of students in school.
"""


def register_check(register: dict) -> int:
    count = 0
    for k, v in register.items():
        if v == "yes":
            count += 1
    return count


register = {"Michael": "yes", "John": "no", "Peter": "yes", "Mary": "yes"}

print(register_check(register))
