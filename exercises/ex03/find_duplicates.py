"""Finding duplicate letters in a word."""

__author__ = "730396516"

word: str = input("Enter a word: ")
i: int = 0
length: int = len(word)
j: int = length - 1
dup: bool = j == i
other = "False"


while i < length:
    j: int = length - 1
    while j > i:
        if word[j] == word[i]:
            other = "True"
        j = j - 1
    i += 1

print("Found duplicate: " + other)