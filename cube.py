"""
This module defines a Cube class, and prints a list of 25
randomly chosen faces of the cube.
"""

import random


# Number of moves in scramble algorithm.
K = 25


""" A list of possible modifications on a move. To be appended to a
face value like so: 'U2'.
"""
MODS = ["2", "'"]


class Cube:
    """
    Class attribute: A list of faces on the cube,
    U : Up, D : Down (bottom face), and so on.
    """
    FACES = ['U', 'D', 'F', 'R', 'B', 'L']

    def __init__(self, order):
        self.order = order

    # Instance method randomly chooses from FACES, K times
    def __str__(self):
        scramble_alg = random.choices(Cube.FACES, k = K)
        return f'Your scramble: {scramble_alg}'


three_by_three = Cube(3)

print(three_by_three)
