# -*- coding: utf-8 *-*

FIRST_TEN = ["", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    '''
        Takes a number as an integer and returns
        a string that is the representation of the
        number.
    '''
    if number < 10:
        return FIRST_TEN[number]
    if number < 20:
        return SECOND_TEN[number-10]
    if number < 100:
        if number%10 == 0:
            return OTHER_TENS[(number//10)-2]
        else:
            return OTHER_TENS[(number//10)-2] + ' ' + checkio(number%10)
    else:
        if number%100 == 0:
            return FIRST_TEN[number//100] + ' hundred'
        else:
            return FIRST_TEN[number//100] + ' hundred ' + checkio(number%100)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"

