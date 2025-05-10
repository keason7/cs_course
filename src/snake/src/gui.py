"""Function for the GUI and user menu."""

import os
import time

import keyboard


def clear():
    """Clear the terminal screen by using the command:

    - `cls` if OS is windows.
    - `clear` if not.
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome():
    """Display game logo and welcome message"""

    clear()

    ascii_snake = r"""
        Y
      .-^-.
     /     \      .- ~ ~ -.
    ()     ()    /   _ _   `.                     _ _ _
     \_   _/    /  /     \   \                . ~  _ _  ~ .
       | |     /  /       \   \             .' .~       ~-. `.
       | |    /  /         )   )           /  /             `.`.
       \ \_ _/  /         /   /           /  /                `'
        \_ _ _.'         /   /           (  (
                        /   /             \  \
                       /   /               \  \
                      /   /                 )  )
                     (   (                 /  /
                      `.  `.             .'  /
                        `.   ~ - - - - ~   .'
                           ~ . _ _ _ _ . ~
    """
    # compute longest ascii snake line
    longest_line = max(len(line) for line in ascii_snake.splitlines())

    # display logo and welcome text
    print("=" * longest_line)
    print("SNAKE GAME".center(longest_line))
    print(ascii_snake)
    print("=" * longest_line + "\n")


def menu():
    """Print game menu and wait for the user to press some keys.

    Returns:
        str: Key name.
    """
    print("Press:")
    print("- p to play a game")
    print("- esc to quit")

    while True:
        if keyboard.is_pressed("p"):
            return "p"
        elif keyboard.is_pressed("esc"):
            return "esc"

        # avoid cpu overload
        time.sleep(0.01)


def draw(width, height, snake_coords, food_coords):
    """Draw snake, food and map.

    Args:
        width (int): Map width.
        height (int): Map height.
        snake_coords (list): Snake coordinates of shape [(x1, y1), (x2, y2), ...] where first
                             coordinate is snake head.
        food_coords (tuple): Food coordinate of shape (x, y).
    """
    clear()
    print("=" * (width + 2))
    for y in range(height):
        line = ""
        for x in range(width):
            if (x, y) == snake_coords[0]:
                line += "0"
            elif (x, y) in snake_coords:
                line += "O"
            elif (x, y) == food_coords:
                line += "X"
            else:
                line += " "
        print("|" + line + "|")
    print("=" * (width + 2))
