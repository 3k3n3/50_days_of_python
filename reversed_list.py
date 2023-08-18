"""
You are given a string of words. Some of the words in the string contain
uppercase letters. Write a code that will return all the words that have 
an uppercase letter. Your code should return a list of the words.
"""


def reversed_list(str1: str) -> list:
    new = []
    for i in str1.split():
        for j in i:
            if j.isupper():
                i = "".join([x for x in reversed(i)])
                new.append(i)
                break
    return new


str1 = "leArning is hard, bUt if You appLy youRself you can achieVe success"

print(reversed_list(str1))
