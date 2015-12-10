from math import ceil

def add_cost(nb_min):
    '''
        Returns the cost of a day.
        The price for each minute is
        1 coin for the first 100 minutes
        and 2 coins after.
    '''
    if nb_min > 100:
        return (nb_min - 100) * 2 + 100
    else:
        return nb_min


def total_cost(calls):
    '''
        Returns the cost of all calls.
        All calls are rounded to the nearest
        minute (for example 61s will count
        as 2 minutes).
    '''
    nb_min = 0
    total = 0
    day = ''
    for call in calls:
        day_call = call[:10]
        duration = int(call[20:])
        if day_call == day:
            nb_min += ceil(duration / 60)
        else:
            total += add_cost(nb_min)
            day = day_call
            nb_min = ceil(duration / 60)
    total += add_cost(nb_min)

    return total


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost(("2014-01-01 01:12:13 181",
                       "2014-01-02 20:11:10 600",
                       "2014-01-03 01:12:13 6009",
                       "2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost(("2014-02-05 01:00:00 1",
                       "2014-02-05 02:00:00 1",
                       "2014-02-05 03:00:00 1",
                       "2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost(("2014-02-05 01:00:00 60",
                       "2014-02-05 02:00:00 60",
                       "2014-02-05 03:00:00 60",
                       "2014-02-05 04:00:00 6000")) == 106, "Precise calls"
