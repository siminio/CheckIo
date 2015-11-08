# -*- coding: utf-8 *-*

import re

def checkio(password):
    '''
        Takes a string and returns a boolean that
        says if this is a good password or not.
    '''
    if re.search("[0-9]+", password) != None:
        has_number = True
    else:
        has_number = False
    has_good_length = len(password) >= 10  
    if re.search("[A-Z]+", password) != None:
        has_capital_letter = True
    else:
        has_capital_letter = False
    if re.search("[a-z]+", password) != None:
        has_small_letter = True
    else:
        has_small_letter = False
        
    return has_number and has_good_length and has_capital_letter and has_small_letter



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"