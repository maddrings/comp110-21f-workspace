"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730396516"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune = str(print("Your fortune cookie says..."))
phrase = int(randint(1, 4))
if phrase == 1:
    print("This is going to be the best day EVER!!")
else:
    if phrase == 2:
        print("Good people are coming your way!")
    else:
        if phrase == 3:
            print("Good vibes only!")
        else:
            if phrase == 4:
                print("The best is yet to come!")
            
print("Now, go spread positive vibes!")