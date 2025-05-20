# TP Devine mon âge

## Solution

```python
import random
import time


def main():
    # ages minimums et maximums
    age_min = 0
    age_max = 77

    # choose an int between age_min et age_max included
    age_target = random.randint(age_min, age_max)

    # while loop stop condition
    age_found = False

    # while the target age has not been found, do the loop
    while not age_found:
        # user choose an age
        age_guess = input("Devinez l'âge...\n")
        print()

        # convert str to float and then to int
        # if we convert directly to int the program crash when the user
        # enter something like: 25.0 as it is a float
        # int(float()) ensure that 25 or 25.0 strings are converted to int
        age_guess = int(float(age_guess))

        # the target age is higher than the guess
        if age_target > age_guess:
            # display "3 ...", "2 ...", "1 ..." with 1s interval
            # before giving a clue about the target age
            for i in range(3):
                print(f"{3 - i} ...")
                time.sleep(1)

            # display clue about target age
            print("Je suis plus vieux.\n")

        # the target age is lower than the guess
        elif age_target < age_guess:
            # display "3 ...", "2 ...", "1 ..." with 1s interval
            # before giving a clue about the target age
            for i in range(3):
                print(f"{3 - i} ...")
                time.sleep(1)

            # display clue about target age
            print("Je suis plus jeune.\n")

        # the target age is not higher or lower so we found the correct age
        else:
            # user found target age, we can stop the while loop and display the target age
            age_found = True
            print(f"Bravo ! J'ai {age_target} ans")


if __name__ == "__main__":
    main()
```
