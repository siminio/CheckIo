# -*- coding: utf-8 *-*

def checkio(number):
    '''
        Takes the number of bird portions and returns
        the number of pigeons that can be fed.        
    '''
    nb_birds = 0
    count = 0
    while 1:
        count += 1
        nb_birds += count
        if number >= nb_birds:
            number -= nb_birds
        elif number > nb_birds - count:
            return number
        else:
            return nb_birds - count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"