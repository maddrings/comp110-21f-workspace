"""An exercise in remainders and boolean logic."""

__author__ = "730396516"


# Begin your solution here...
choice: int = int(input("Enter an int: "))
tar: str = "TAR"
heels: str = "HEELS"
i = 0

while i == 0:
    if choice % 2 == 0:
        if choice % 7 == 0:
            print(tar + " " + heels)
            i = i + 1
        else:
            print(tar)
            i = i + 1
    else:
        if choice % 7 == 0:
            print(heels)
            i = i + 1
        else:
            print("CAROLINA")
        i = i + 1
    i = i + 1