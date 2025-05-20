# TP Jeu du pendu

## Solution

```python
"""Hangman's game code."""

import os
import random
import time

import requests
from unidecode import unidecode


def clear(sleep=None):
    """Clear the terminal screen by using the command:
    - `cls` if OS is windows.
    - `clear` if not.

    Args:
        sleep (float or None, optional): Number of seconds to wait before
            clearing the screen. Defaults to None.
    """
    # wait for x seconds if sleep is not None value (default value)
    if sleep is not None:
        time.sleep(sleep)

    # use os to execute a terminal command (cls or clear)
    os.system("cls" if os.name == "nt" else "clear")


def normalize_word(word):
    """Replace letters with accents and set ord to lowercase.

    Args:
        word (str): Word to guess.

    Returns:
        str: Normalized word.
    """
    # use unidecode() to remove accent and lower() to set to lowercase
    return unidecode(word).lower()


def get_random_word(url):
    """Get a random french word and associated word category.

    Args:
        url (str): Target url to fetch word data.

    Returns:
        str: Word.
        str: Category.
    """
    # fallback words and categories if get form url crash
    fallback = (
        ("château", "lieu"),
        ("école", "endroit"),
        ("ordinateur", "objet"),
        ("voiture", "transport"),
        ("arbre", "nature"),
    )

    # execute this first
    try:
        # get content for url with None timeout (don't wait before executing get)
        response = requests.get(url, timeout=None)

        # if an error occur, this will returns a HTTPError
        response.raise_for_status()

        # convert response to json
        response_json = response.json()

        # get word and category
        word = response_json[0]["name"]
        category = response_json[0]["categorie"]

        # return normalized word and category set to lowercase
        return normalize_word(word), category.lower()

    # execute this if there is a crash inside try instruction
    except requests.exceptions.HTTPError as error_message:
        print("Erreur de récupération du mot:", error_message, "\nMot de secours utilisé.")

        # make a random choice in fallback data
        word, category = random.choice(fallback)

        # return normalized word and category
        return normalize_word(word), category


def display_word(word, used_letters):
    """Display a hangman word:
    - Guessed letters are displayed.
    - Unguessed letters are displayed as "_".

    Args:
        word (str): Word to guess.
        used_letters (set): Set of previously used letters.

    Returns:
        str: Hangman word ready for display.
    """
    # initialize list of letters to display
    display_letters = []

    # iterate over each letter of the word
    for letter in word:
        # add letter if it has been guessed
        if letter in used_letters:
            display_letters.append(letter)

        # add "_" otherwise
        else:
            display_letters.append("_")

    # join all letters of the list to make a single str with a space between each letter
    # ['_', 'b', '_', '_', '_', '_', '_', 'e'] -> "_ b _ _ _ _ _ e"
    return " ".join(display_letters)


def get_guess(used_letters):
    """Get guess from the user and verify validity.

    Args:
        used_letters (set): Set of previously used letters.

    Returns:
        str or None: Return single letter str or None if input is not valid.
    """
    # get user guess as lowercase
    user_guess = input("Proposez une lettre: ").lower()

    # if input does not have 1 caracter or if input is not a letter
    # print error message and return None
    if len(user_guess) != 1 or not user_guess.isalpha():
        print("❌ Entrez une seule lettre alphabétique.")
        return None

    # if letter has already been used
    # print error message and return None
    if user_guess in used_letters:
        print("❌ Lettre déjà utilisée.")
        return None

    # return letter if user input is valid
    return user_guess


def is_word_found(word, used_letters):
    """Check if the word has been found.

    Args:
        word (str): Word to guess.
        used_letters (set): Set of previously used letters.

    Returns:
        bool: Return True if the word has been guessed, False otherwise.
    """
    # iterate on word letters
    for letter in word:
        # if current letter is not in used letters
        # word has not been found yet, return False
        if letter not in used_letters:
            return False

    # all word letters are in used_letters, word has been found
    # return True
    return True


def print_status(game_state):
    """Print current game state:
    - Word category (hint).
    - Word with hidden letters if these letters are not found yet.
    - Previously used letters.
    - Remaining lives.

    Args:
        game_state (dict): Game state dictionary.
    """
    display = display_word(game_state["word"], game_state["used_letters"])

    print(f"Catégorie: {game_state["category"]}")
    print(f"Mot: {display}")
    print(f"Lettres utilisées: {", ".join(sorted(game_state["used_letters"]))}")
    print(f"Vies restantes: {game_state["lives"]}\n")


def hangman():
    """Main hangman game function."""

    # clear terminal screen
    clear()

    # try get word and category from url or fallback
    url = "https://trouve-mot.fr/api/random"
    word, category = get_random_word(url)

    # declare game state dictionary
    game_state = {
        "word": word,
        "used_letters": set(),
        "lives": 7,
        "category": category,
    }

    # welcome message
    print(f"Bienvenue au Pendu ! Le mot contient {len(word)} lettres.\n")

    # keep playing while the user has lives
    while game_state["lives"] > 0:
        # print current game state
        print_status(game_state)

        # get user guess from keyboard
        user_guess = get_guess(game_state["used_letters"])

        # if user guess is not valid, skip current iteration
        # and go next while loop iteration (continue keyword)
        if user_guess is None:
            # wait and clear terminal screen
            clear(sleep=2.0)

            # dont't execute code after this
            # we go back to while loop beginning
            continue

        # add valid user_guess letter to used letter
        game_state["used_letters"].add(user_guess)

        # user guess letter is in word letters
        if user_guess in game_state["word"]:
            # the user has found a letter
            print("✅ Bien joué !")

            # since user has found a letter, we need to check if word has been completly found
            if is_word_found(game_state["word"], game_state["used_letters"]):
                # wait and clear terminal screen
                clear(sleep=2.0)

                # user has found the word
                print(f"Gagné ! Le mot était: {game_state['word']}")

                # return (None by default) so we can exit the function and go back to main
                return
        else:
            # the user did not found a letter
            print("❌ Mauvaise réponse.")

            # decrease by 1 the user number of lives
            game_state["lives"] -= 1

        # wait and clear terminal screen
        clear(sleep=2.0)

    # while loop become False since user has 0 lives
    # user lost game
    print(f"Perdu ! Le mot était: {game_state['word']}")


if __name__ == "__main__":
    hangman()
```
