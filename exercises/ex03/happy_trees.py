"""Drawing forests in a loop."""

__author__ = "730396516"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: str = input("Depth: ")
count = int(depth)
i = 1
tree = ""
other = ""

while i <= count:
    if count > 0:
        if count == 1:
            tree = TREE
            space = ""
        else:
            j = 0
            while j < count:
                space = TREE + " "
                other = (" " + TREE)
                tree = TREE
                print((space + tree) * j)
                count = count - 1
                j = j + 1
    else:
        tree = tree
        space = ""
    i += 1
    print(((tree + " ") * i) + TREE)