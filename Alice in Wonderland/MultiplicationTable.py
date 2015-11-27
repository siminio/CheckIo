# -*- coding: utf-8 *-*

def do_ope(ope, bit1, bit2):
    '''
        Returns the result of the logical operation
        between two bits ("0"/"1").
    '''
    if ope == 'and':
        if bit1 == bit2:
            return bit1
        else:
            return "0"
    elif ope == 'or':
        if bit1 == bit2 == "0":
            return "0"
        else:
            return "1"
    elif ope == 'xor':
        if (bit1 == "1" and bit2 == "0") or (bit1 == "0" and bit2 == "1"):
            return "1"
        else:
            return "0"


def checkio(first, second):
    '''
        Returns the sum of the three operations:
        OR, XOR, AND of two numbers which are integers.
    '''
    # Binary representation of the inputs    
    bin1 = bin(first)[2:]
    bin2 = bin(second)[2:]
    result = 0
    for ope in ['and', 'or', 'xor']:
        for bit1 in bin1:
            bin_result = ""
            for bit2 in bin2:
                bin_result += do_ope(ope, bit1, bit2)
            result += int(bin_result, 2)    
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 6) == 38
    assert checkio(2, 7) == 28
    assert checkio(7, 2) == 18