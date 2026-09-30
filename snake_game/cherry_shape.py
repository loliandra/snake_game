from turtle import Shape
import math


def circle_points(x, y, radius):
    return tuple(
        (
            x + radius * math.cos(math.radians(angle)),
            y + radius * math.sin(math.radians(angle))
        )
        for angle in range(0, 360, 15)
    )


def create_cherry_shape():
    cherries = Shape("compound")

    # Веточки
    cherries.addcomponent(
        ((-7, -3), (-6, 0), (2, 14), (4, 14)),
        "#8EAD83", "#8EAD83"
    )
    cherries.addcomponent(
        ((7, -4), (9, -4), (4, 14), (2, 14)),
        "#8EAD83", "#8EAD83"
    )

    # Листочек
    cherries.addcomponent(
        ((3, 13), (7, 19), (13, 20), (11, 15), (7, 12)),
        "#A8C99B", "#A8C99B"
    )

    # Ягодки
    cherries.addcomponent(
        circle_points(-7, -5, 7),
        "#E98BA3", "#E98BA3"
    )
    cherries.addcomponent(
        circle_points(8, -7, 7),
        "#DA708F", "#DA708F"
    )

    # Блики
    cherries.addcomponent(
        circle_points(-9, -2, 1.8),
        "#FFE1E9", "#FFE1E9"
    )
    cherries.addcomponent(
        circle_points(6, -4, 1.8),
        "#FFE1E9", "#FFE1E9"
    )

    return cherries