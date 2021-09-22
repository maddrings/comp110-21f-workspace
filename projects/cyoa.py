"""Choose your own adventure experience."""

from random import randint

game: list[str] = ["rock", "paper", "scissors"]

player: str = ""
rock: str = "rock"
paper: str = "paper"
scissors: str = "scissors"
points = int
comp_points = int
a: int = 0
version = int


def greet() -> None:
    player = str(input("Enter player's name: "))
    print(f"Hello {player}!! Let's play rock-paper-scissors! When prompted, enter rock, paper, or scissors. If you beat me, you get a point. If I beat you, I get a point. First to receive 3 points wins the game. Ready? Let's go!")


def pro() -> None:
    points = 0
    comp_points = 0
    while (points < 3) and (comp_points < 3):
        choice = str(input("rock...paper...scissors...SHOOT!!!: "))
        computer = game[randint(0, 2)]
        print(computer)
        if choice == rock and computer == paper:
            points = points
            comp_points = comp_points + 1
        if choice == rock and computer == scissors:
            points = points + 1
            comp_points = comp_points
        if choice == paper and computer == rock:
            points = points + 1
            comp_points = comp_points
        if choice == paper and computer == scissors:
            points = points
            comp_points = comp_points + 1
        if choice == scissors and computer == rock:
            points = points
            comp_points = comp_points + 1
        if choice == scissors and computer == paper:
            points = points + 1
            comp_points = comp_points
        if choice == computer:
            points = points
            comp_points = comp_points
        print(f"Your score: {points}")
        print(f"My score: {comp_points}")
    if points == 3:
        print("YOU WIN :)")
    if comp_points == 3:
        print("YOU LOSE :(")


def fun(points: int) -> int:
    comp_points = 0
    while (points < 3) and (comp_points < 3):
        choice = str(input("rock...paper...scissors...SHOOT!!!: "))
        computer = game[randint(0, 2)]
        print(computer)
        if choice == rock and computer == paper:
            points = points
            comp_points = comp_points + 1
        if choice == rock and computer == scissors:
            points = points + 1
            comp_points = comp_points
        if choice == paper and computer == rock:
            points = points + 1
            comp_points = comp_points
        if choice == paper and computer == scissors:
            points = points
            comp_points = comp_points + 1
        if choice == scissors and computer == rock:
            points = points
            comp_points = comp_points + 1
        if choice == scissors and computer == paper:
            points = points + 1
            comp_points = comp_points
        if choice == computer:
            points = points
            comp_points = comp_points
        print(f"Your score: {points}")
        print(f"My score: {comp_points}")
    if points == 3:
        print("YOU WIN :)")
    if comp_points == 3:
        print("YOU LOSE :(")
    return points


def main() -> None:
    version = int(input("Which version (1 or 2) of the game would you like to play? "))
    while version == 1:
        greet()
        pro()
        cont = str(input("Would you like to play again? Enter 'Yes' or 'No'. "))
        if cont == str("No"):
            print("GAME OVER")
            version = version + 1
        else:
            while cont == str("Yes"):
                new_version = int(input("Which version (1 or 2) of the game would you like to play? "))
                if new_version == 1:
                    pro()
                if new_version == 2:
                    fun(0)
                cont = str(input("Would you like to play again? Enter 'Yes' or 'No'."))
    while version == 2:
        greet()
        fun(0)
        cont = str(input("Would you like to play again? Enter 'Yes' or 'No'. "))
        if cont == str("No"):
            print("GAME OVER")
            version = version + 1
        else:
            while cont == str("Yes"):
                new_version = int(input("Which version (1 or 2) of the game would you like to play? "))
                if new_version == 1:
                    pro()
                if new_version == 2:
                    fun(0)
                cont = str(input("Would you like to play again? Enter 'Yes' or 'No'."))


if __name__ == "__main__":
    main()