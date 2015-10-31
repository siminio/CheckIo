# -*- coding: utf-8 *-*

def checkio(first, second):
	"""
		Returns the common words sorted by alphabetical order
		between 2 lists of words delimited by comma.
	"""
    set_words1 = set(first.split(','))
    set_words2 = set(second.split(','))
    set_result = set_words1.intersection(set_words2)
    return ",".join(sorted(list(set_result)))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"