# -*- coding: utf-8 *-*

def checkio(number):
	"""
		Multiply each digit in the list and skip 0.
	"""
	list_num = [int(c) for c in str(number) if int(c) != 0]
	result = 1
	for num in list_num:
		result *= num
	return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1