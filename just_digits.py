"""
Write a function called just_digits that reads the text from the 
python.csv file and returns only digit elements from the file.
"""


def just_digits():
    dg = []
    with open("python.csv") as f:
        for i in f.readlines():
            for j in i.split(" "):
                if j.isdigit() == True:
                    dg.append(j)

    return ", ".join(dg)


print(just_digits())
