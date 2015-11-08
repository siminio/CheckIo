# -*- coding: utf-8 *-*

def checkio(data):
    '''
        Function that takes an array and returns
        the same array with only the elements
        that appear more than once.
    '''         
    result = []        
    for elem in data:
        if data.count(elem) > 1:
            result.append(elem)    
    return result


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(checkio([1]), list), "The result must be a list"
    assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3], "1st example"
    assert checkio([1, 2, 3, 4, 5]) == [], "2nd example"
    assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5], "3rd example"
    assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9], "4th example"
