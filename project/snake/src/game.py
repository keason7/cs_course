"""Snake game logic functions."""

import random as rd
import time

import keyboard

from src.gui import draw


def get_action(direction):
    """Return action to apply based of user input key.

    Args:
        direction (str): Current snake direction such as "up", "left", ...

    Returns:
        str or None: Action key to perform or None to do nothing.
    """
    # move the snake to the desired direction except if current direction is the invert
    # (ex: snake can't go up if current direction is down)
    if keyboard.is_pressed("up") and direction != "down":
        return "up"
    elif keyboard.is_pressed("down") and direction != "up":
        return "down"
    elif keyboard.is_pressed("left") and direction != "right":
        return "left"
    elif keyboard.is_pressed("right") and direction != "left":
        return "right"
    # exit the game
    elif keyboard.is_pressed("esc"):
        return "esc"
    return None


def init_food(width, height, snake_coords):
    """Initialize a random food coordinate.

    Args:
        width (int): Map width.
        height (int): Map height.
        snake_coords (list): Snake coordinates of shape [(x1, y1), (x2, y2), ...] where first
                             coordinate is snake head.

    Returns:
        tuple: Food coordinate of shape (x, y).
    """
    # list of all possible coordinates in map such as:
    # [(x1, y1), (x2, y2), ...]
    map_coords = [(x, y) for x in range(width) for y in range(height)]

    # get a list of coordinates on the map that are not occupied by the snake
    # we transform both coords into setsand make the difference such as:
    # set_A = {1, 2, 3, 4}
    # set_B = {3, 4, 5}
    # set_A - set_B = {1, 2} ----> give me all elements in the set A that are not in the set B
    food_coords = list(set(map_coords) - set(snake_coords))

    return rd.choice(food_coords)


def snake_game(width=15, height=15):
    """Snake game.

    Args:
        width (int, optional): Map width. Defaults to 15.
        height (int, optional): Map height. Defaults to 15.

    Returns:
        int: Snake score, which is snake length.
    """
    # initialize possible directions of the snake
    directions = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }

    # initialize snake parameters
    # - snake coordinates in map
    # - snake speed (every n seconds the snake move)
    # - snake direction
    snake = {
        "coords": [(5, 5), (4, 5), (3, 5)],
        "speed": 0.15,
        "direction": "right",
    }

    # compute current time as float value
    # (ex: 1745930962.517367)
    previous_time = time.time()

    # initialize a food coordinate within map and not at a snake coord
    food_coords = init_food(width, height, snake["coords"])

    while True:
        # capture key press event (asynchronous)
        key = get_action(snake["direction"])

        # quit game and return score
        if key == "esc":
            return len(snake["coords"])

        # a relevant key has been pressed (up, down, left, right)
        if key is not None:
            # store wanted next direction for the snake
            snake["direction"] = key

        # compare current time and previous time
        # if it is superior to snake speed, we should
        # update game parameters and draw to refresh current game state
        if time.time() - previous_time >= snake["speed"]:
            # update previous time if we refresh game state
            previous_time = time.time()

            # get wanted next direction and current snake head
            direction_x, direction_y = directions[snake["direction"]]
            snake_head_x, snake_head_y = snake["coords"][0]

            # compute where is the snake head at next iteration
            new_head = (snake_head_x + direction_x, snake_head_y + direction_y)

            # it's game over if:
            # - snake head at next iteration is in snake body
            # - snake head at next iteration is outside map boundaries
            if (
                new_head in snake["coords"]
                or not (0 <= new_head[0] < width)
                or not (0 <= new_head[1] < height)
            ):
                return len(snake["coords"])

            # next head position id valid so we insert it are snake position 0:
            # ex: [(x0, y0), (x1, y1), (x2, y2)]
            #     ->
            #     [(x_new_head, y_new_head), (x0, y0), (x1, y1), (x2, y2)]
            snake["coords"].insert(0, new_head)

            # new head id on current food, so we reset food coordinate
            if new_head == food_coords:
                food_coords = init_food(width, height, snake["coords"])
            # the new head do not eat food
            # since we added the new head before we can cut the last tail element
            # to keep the same snake length
            else:
                snake["coords"].pop()

            # draw map, snake and food
            draw(width, height, snake["coords"], food_coords)

        # avoid cpu overload
        time.sleep(0.01)
