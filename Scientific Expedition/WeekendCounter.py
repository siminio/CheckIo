from datetime import date, timedelta

def checkio(from_date, to_date):
    """
        Count the days of rest
        (Saturdays and Sundays).
    """
    count = 0
    date_to_check = from_date
    #Loop for each day from from_date to to_date
    while date_to_check <= to_date:
        if date_to_check.weekday() in [5,6]:
            count += 1
        date_to_check = date_to_check + timedelta(days = 1)
    return count

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"