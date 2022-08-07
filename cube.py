"""
This module defines a Cube class, and prints a list of 25
randomly chosen faces of the cube.
"""

import random


# Number of moves in scramble algorithm.
K = 25


class Cube:
    """
    Class attribute: A list of faces on the cube,
    U : Up, D : Down (bottom face), and so on.
    """
    def __init__(self, order):
        self.order = order

    # Instance method randomly chooses from FACES, K times
    @staticmethod
    def generate_scramble():
        scramble = [RandomScrambleStep()]
        while len(scramble) < K:
            step = RandomScrambleStep()
            if scramble[-1].face != step.face:
                scramble.append(step)
        return scramble


class RandomScrambleStep:
    """
    Is a single turn of the cube.
    """
    MODS = ["2", "'", ""]  # A list of possible modifications on a turn
    FACES = ['U', 'D', 'F', 'R', 'B', 'L']

    def __init__(self):
        self.face = random.choice(RandomScrambleStep.FACES)
        self.mod = random.choice(RandomScrambleStep.MODS)

    def __str__(self):
        return f'{self.face}{self.mod}'

    def __repr__(self):
        return self.__str__()
