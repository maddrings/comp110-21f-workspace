"""Choose your own adventure experience."""

__author__ = "730396516"

from random import randint

game: list[str] = ["rock", "paper", "scissors"]

STAR_EYES: str = '\U0001F929'
SAD_FACE: str = '\U0001F614'

player: str = ""
rock: str = "rock"
paper: str = "paper"
scissors: str = "scissors"
points: int = 0
comp_points: int = 0
version: int = 0


def greet() -> None:
    """Greeting to player with instructions for game."""
    global player
    player = str(input("Enter player's name: "))
    print(f"Hello {player}!! Let's play rock-paper-scissors! When prompted, enter 'rock', 'paper', or 'scissors'. If you beat me, you get a point. If I beat you, I get a point. First to receive 3 points wins the game. Ready? Let's go!")


def pro() -> None:
    """Version 1 of game."""
    global player
    global points
    global comp_points
    while (points < 3) and (comp_points < 3):
        choice = str(input("rock...paper...scissors...SHOOT!!!: "))
        computer = game[randint(0, 2)]
        print(f"My turn: {computer}")
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
        print(f"{player}'s score: {points}")
        print(f"My score: {comp_points}")
    if points == 3:
        print(f"Good job {player}! YOU WIN {STAR_EYES}{STAR_EYES}{STAR_EYES}")
    if comp_points == 3:
        print(f"Sorry, {player}. YOU LOSE {SAD_FACE}{SAD_FACE}{SAD_FACE}")


def fun(score: int) -> int:
    """Version 2 of game."""
    global player
    global points
    global comp_points
    while (points < 3) and (comp_points < 3):
        choice = str(input("rock...paper...scissors...SHOOT!!!: "))
        computer = game[randint(0, 2)]
        print(f"My turn: {computer}")
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
        print(f"{player}'s score: {points}")
        print(f"My score: {comp_points}")
    if points == 3:
        print(f"Good job {player}! YOU WIN {STAR_EYES}{STAR_EYES}{STAR_EYES}")
    if comp_points == 3:
        print(f"Sorry, {player}. YOU LOSE {SAD_FACE}{SAD_FACE}{SAD_FACE}")
    return points


def main() -> None:
    """Main function."""
    global points
    global comp_points
    version = int(input("Which version (1 or 2) of the game would you like to play? "))
    while version == 1:
        greet()
        pro()
        cont = str(input("Would you like to play again? Enter 'Yes' or 'No'. "))
        if cont == str("No"):
            version = 0
            print("GAME OVER")
        else:
            while cont == str("Yes"):
                points = 0
                comp_points = 0
                new_version = int(input("Which version (1 or 2) of the game would you like to play? "))
                if new_version == 1:
                    pro()
                if new_version == 2:
                    fun(points)
                cont = str(input("Would you like to play again? Enter 'Yes' or 'No'. "))
                if cont == str("No"):
                    version = 0
                    print("GAME OVER")
    while version == 2:
        greet()
        fun(points)
        cont = str(input("Would you like to play again? Enter 'Yes' or 'No'. "))
        if cont == str("No"):
            version = 0
            print("GAME OVER")
        else:
            while cont == str("Yes"):
                points = 0
                comp_points = 0
                new_version = int(input("Which version (1 or 2) of the game would you like to play? "))
                if new_version == 1:
                    pro()
                if new_version == 2:
                    fun(points)
                cont = str(input("Would you like to play again? Enter 'Yes' or 'No'. "))
                if cont == str("No"):
                    version = 0
                    print("GAME OVER")


if __name__ == "__main__":
    main()