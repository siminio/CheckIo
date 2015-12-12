# -*- coding: utf-8 *-*

def checkio(opacity):
    """
        Determines the age of a ghost.
        10000 is a completely opaque newborn ghost (0 years old)
        and 0 is completely transparent ghost (of an unknown age).
        On every birthday, a ghost's opacity is reduced by a
        number of units equal to its age when its age is a
        Fibonacci number or increased by 1 if it is not.
    """
    list_fib_num = [0,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946]
    temp_opacity = 10000
    for year in range(1, 5000):
        if opacity == temp_opacity:
            break
        if year in list_fib_num:
            temp_opacity -= year
        else:
            temp_opacity += 1
    return year - 1

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"