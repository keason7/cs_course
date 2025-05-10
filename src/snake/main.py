"""Snake game main code."""

from src.game import snake_game
from src.gui import clear, menu, welcome


def main():
    """Snake game"""
    # display welcome message and logo
    welcome()

    # initialize a best score to -infinity
    best_score = float("-inf")

    # keep playing until the user decide to quit
    while True:
        # display the game menu and wait for user choice
        key = menu()

        # exit game
        if key == "esc":
            clear()
            return False

        # play game
        else:
            # play game and get user score
            score = snake_game(width=20, height=20)
            clear()

            # update best score if the user beat it
            if best_score < score:
                best_score = score

            # display scores
            print(f"Best score {best_score}")
            print(f"Your score {score}\n")


if __name__ == "__main__":
    main()
