"""Repeating a beat in a loop."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"


# Begin your solution here...
beat = str(input("What beat do you want to repeat? "))
number = int(str(input("How many times do you want to repeat it? ")))
maximum = int(number + 1)
counter: int = 1
none = str("No beat...")
s: str = ""


while counter < maximum:
    if number < 1:
        s: str(print("No beat..."))
    else:
        if number >= 1:
            s = s + beat
        if number < maximum:
            s = s + " "
    counter = counter + 1
print(s)
