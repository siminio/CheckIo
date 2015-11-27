def checkio(time_string):
    '''
        Takes a time which format is HH:mm:ss
        and returns this time in morse.
    '''
    hour, minute, second = map(int, time_string.split(':'))
    h1 = '{:02b}'.format(hour//10)
    h2 = '{:04b}'.format(hour%10)
    h = h1 + ' ' + h2

    m1 = '{:03b}'.format(minute//10)
    m2 = '{:04b}'.format(minute%10)
    m = m1 + ' ' + m2

    s1 = '{:03b}'.format(second//10)
    s2 = '{:04b}'.format(second%10)
    s = s1 + ' ' + s2

    time_string_morse = h + ' : '  + m + ' : ' + s
    time_string_morse = time_string_morse.replace('1', '-')
    time_string_morse = time_string_morse.replace('0', '.')

    return time_string_morse

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

