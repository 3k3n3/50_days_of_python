"""
Write a function called multiply_words that takes a string as an 
argument and multiplies the length of each word in the string by 
the length of other words in the string.
However, your function should only multiply words will all lowercase
letters. If a word has one upper case letter, it should be ignored. 
"""


def multiply_words(words: str) -> str:
    count = 1
    new = []
    for word in words.split():
        if not any(char.isupper() for char in word):
            new.append(f"{word} ({len(word)})")
            count *= len(word)

    return f'{count} - {" ".join(new)}'


s1 = "love live and laugh"
s2 = "Hate war love Peace"
print(multiply_words(s1))
print(multiply_words(s2))
