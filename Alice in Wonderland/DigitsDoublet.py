# -*- coding: utf-8 *-*

def close_numbers(num1, num2):
    '''
        Takes two numbers (integers) as inputs
        and retuns True if there is just one
        digit different between the two numbers.
    '''
    str_num1 = str(num1)
    str_num2 = str(num2)
    compteur = 0
    for i in range(len(str_num1)):
        if str_num1[i] != str_num2[i]:
            compteur += 1
    if compteur == 1:
        return True
    else:
        return False

def checkio(numbers):
    '''
        Takes a list of numbers (integers) as input
        and returns the shortest list of numbers which
        links the first and the last numbers by changing
        one digit at the time sorted by ascending order.
    '''
    # Start with the first number
    queue = [numbers[0],]
    dict_nums = {}

    for num_to_test in queue:
        # End when reaching the last number
        if num_to_test == numbers[-1]:
            break
        else:
            for num in numbers:
                if close_numbers(num_to_test, num):
                    queue.append(num)
                    if num not in dict_nums.keys():
                        dict_nums[num] = num_to_test
                        
    # Makes the path from the last number to the first number
    path_nums = [numbers[-1],]
    num = numbers[-1]
    while num != numbers[0]:
        num = dict_nums[num]
        path_nums.append(num)
        
    return list(reversed(path_nums))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
    assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
    assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"


