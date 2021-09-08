"""Counting letters in a string."""

__author__ = "730396516"


# Begin your solution here...

letter = str(input("What letter do you want to search for?: "))
word = str(input("Enter a word: "))
length = int(len(word))
count = 0
i = 0
while i < length:
    if word[i] == letter:
        count = count + 1
    else:
        count = 0
    i = i + 1
print("Count: " + str(count))