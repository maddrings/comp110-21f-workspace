"""Repeating a beat in a loop."""

__author__ = "730396516"


# Begin your solution here...
beat = str(input("What beat do you want to repeat? "))
number = int(str(input("How many times do you want to repeat it? ")))
counter: int = 1
s: str = ""
space = int(number - 1)

if number <= 0:
    print("No beat...")
else:
    while counter <= number:
        if space < number:
            s = s + beat
            space = space + 1
        else:
            s = s + " " + beat
        counter = counter + 1
    print(s)