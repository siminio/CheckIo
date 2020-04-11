def time_converter(time):
    hours, minutes = [int(elem) for elem in time.split(":")]
    if hours < 12:
        if hours == 0:
            hours = 12
        return "{}:{:02d} a.m.".format(hours, minutes)
    else:
        if hours > 12:
            hours -= 12
        return "{}:{:02d} p.m.".format(hours, minutes)
    return time

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))
    print(time_converter('09:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
