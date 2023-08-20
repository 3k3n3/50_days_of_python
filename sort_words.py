"""
Write a function called sort_words that takes a string of words 
as an argument, removes the whitespaces, and returns a list of 
letters sorted in alphabetical order. Letters will be separated by 
commas. All letters should appear once in the list. 
"""


def sort_words(words: str) -> list:
    return sorted(set([char for char in words.replace(" ", "")]))


words = "love life"
print(sort_words(words))
