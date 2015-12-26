# -*- coding: utf-8 *-*

def checkio(num):
    '''
        Returns the roman representation of an integer.
    '''
    list_roman_num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    dict_roman_num = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
                      90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    rest = num
    roman_num = ""
    i = len(list_roman_num) - 1
    #Start from the biggest number to the smallest number
    while i >= 0:
        key = list_roman_num[i]
        nb_iter = rest // key
        roman_num += dict_roman_num[key] * nb_iter
        rest -= key * nb_iter
        i -= 1
    return roman_num

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'