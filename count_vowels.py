"""
Create a function called count_the_vowels. The function 
takes one argument, a string, and returns the number of vowels 
in the string. For example, ‘hello’ should return 2 vowels. If a 
vowel appears in a string more than once it should be counted 
as one. For example, ‘saas’ should return 1 vowel. Your code 
should count lowercase and uppercase vowels.
"""


def count_the_vowels(words: str) -> int:
    vowels = []
    for x in words:
        if x in "AaEeIiOoUu":
            vowels.append(x)

    return len(set(vowels))


words = "helloO"
print(count_the_vowels(words))

words = "saas"
print(count_the_vowels(words))
