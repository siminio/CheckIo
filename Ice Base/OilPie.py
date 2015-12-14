# -*- coding: utf-8 *-*

from fractions import Fraction

def divide_pie(groups):
    '''
        Returns the rest of the pie.
        Each group of drones eats a slice of the pie.
    '''
    nb_drones = sum(map(abs, groups))
    one_normal_part = Fraction(1, nb_drones)
    rest = Fraction(1, 1)
    for group in groups:
        # Group of drones that know the size of the initial pie
        if group > 0:
            rest -= group * one_normal_part
        # Group of drones that think the size of the rest is the size of the initial pie
        else:
            rest -= abs(group) * one_normal_part * rest
    return rest.numerator, rest.denominator

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"