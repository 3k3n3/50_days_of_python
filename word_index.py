"""
Write a function called word_index that takes one argument, 
a list of strings and returns the index of the longest word in the 
list. If there is no longest word (if all the strings are of the same 
length), the function should return zero (0).
"""


def word_index(l: list) -> int:
    words = set([len(x) for x in l])
    if len(words) == 1:
        return 0
    else:
        for x in l:
            if max(words) == len(x):
                return (l.index(x))


words1 = ["Hate", "remorse", "vengeance"]
words2 = ["Love", "Hate"]

print(word_index(words1))
print(word_index(words2))