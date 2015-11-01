# -*- coding: utf-8 *-*

def checkio(str_number, radix):
	"""
		Converts a number which base is the radix in a decimal number.
		If the radix is not correct, then returns -1.
	"""
	list_str_num = list(str_number)
	power = 0
	result = 0
	for i in range(len(list_str_num)):
		str_num = list_str_num[len(list_str_num) -1 - i]
		if str_num.isdigit():
			num = int(str_num)
		else:
			num = (ord(str_num) - 55)
		if num >= radix:
			return -1
		result += num * (radix ** i)
	return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"