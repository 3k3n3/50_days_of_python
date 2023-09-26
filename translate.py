"""
Write a function called translate that takes words and translates them into pig Latin.
Here are the rules: 
1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the 
end. For example, ‘eat’ will become ‘eatyay’ 
2. If a word starts with anything other than a vowel, move 
the first letter to the end and add ‘ay’ to the end. For 
example, ‘day’ will become ‘ayday’.
"""


def translate(words: str) -> str:
    new = []
    for x in words.split():
        if x[0] in "aeiou":
            new.append(f"{x}yay")
        else:
            new.append(f"{x[1:]}{x[0]}ay")

    return " ".join(new)


a = "i love python"
print(translate(a))
