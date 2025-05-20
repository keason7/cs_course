# TP Fractale

## Solution 1.1

```python
from turtle import Screen, Turtle


def initialize_screen(width, height):
    screen = Screen()
    screen.setup(width=width, height=height)

    return screen


def main():
    screen = initialize_screen(width=1.0, height=1.0)

    screen.mainloop()


if __name__ == "__main__":
    main()
```

## Solution 1.2

```python
from turtle import Screen, Turtle


def initialize_screen(width, height):
    screen = Screen()
    screen.setup(width=width, height=height)

    return screen


def initialize_turtle(speed):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(speed)

    return turtle


def main():
    screen = initialize_screen(width=1.0, height=1.0)
    turtle = initialize_turtle(speed=0)

    screen.mainloop()


if __name__ == "__main__":
    main()
```

## Solution 1.3

```python
from turtle import Screen, Turtle


def initialize_screen(width, height):
    screen = Screen()
    screen.setup(width=width, height=height)

    return screen


def initialize_turtle(speed):
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(speed)

    return turtle


def fractal_canopy(turtle, branch_length, branch_width, ratio, depth, angle):
    # condition d'arret de la récursion, lorsque l'on atteint une "feuille d'arbre"
    # si il n'y a plus de niveaux a dessiner, la fonction retourne une valeur None
    # cela empêche la recursion de s'etendre a l'infini
    if depth == 0:
        return None

    # initialise la largeur de la branche courante
    turtle.width(branch_width)
    # dessine la branche courante
    turtle.forward(branch_length)

    # rotate le crayon a droite d'un certain angle
    # cela prepare la branche enfant de droite (appel recursif)
    turtle.right(angle)

    # appel recursif pour dessiner la branche enfant de droite
    # la branche enfant est :
    #   - plus courte (branch_length * ratio)
    #   - plus fine (branch_width * ratio)
    #   - un niveau de profondeur en dessous (depth - 1)
    # comme nous avons tourne a droite avant cet appel
    # la branche enfant est inclinée par rapport au parent
    fractal_canopy(turtle, branch_length * ratio, branch_width * ratio, ratio, depth - 1, angle)

    # rotate le crayon a droite d'un certain angle en passant par la position de depart (2 * angle)
    # cela prepare la branche enfant de gauche (appel recursif)
    turtle.left(angle * 2)

    # appel recursif pour dessiner la branche enfant de gauche
    # la branche enfant est :
    #   - plus courte (branch_length * ratio)
    #   - plus fine (branch_width * ratio)
    #   - un niveau de profondeur en dessous (depth - 1)
    # comme nous avons tourne a gauche avant cet appel
    # la branche enfant est inclinée par rapport au parent
    fractal_canopy(turtle, branch_length * ratio, branch_width * ratio, ratio, depth - 1, angle)

    # rotate le crayon a droite pour retourner a l'angle de la branche parente
    turtle.right(angle)

    # retour a la branche parente
    turtle.backward(branch_length)


def main():
    screen = initialize_screen(width=1.0, height=1.0)
    turtle = initialize_turtle(speed=1)

    # rotate de 90° pour dessiner l'arbre vers le haut de la fenetre
    turtle.left(90)
    # choix de la couleur de dessin
    turtle.color("black")
    # dessin
    fractal_canopy(turtle, branch_length=70, branch_width=5, ratio=0.75, depth=8, angle=33)

    screen.mainloop()


if __name__ == "__main__":
    main()
```

Pour plus de détails sur l'exécution de la fonction voir ce [pdf](./assets/08/explanation_fractal_canopy.pdf) d'explications.
