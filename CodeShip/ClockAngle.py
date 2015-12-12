# -*- coding: utf-8 *-*

def clock_angle(time):
    '''
        Returns the angle in degrees between
        the minute and hour hands.
    '''
    minutes = int(time[-2:])
    heures = int(time[:2]) % 12
    # Angles from the origin
    angle_min = 360 * (minutes / 60)
    heures = heures + (minutes / 60)
    angle_h = 360 * (heures / 12)
    # Difference between the two angles
    angle_diff = abs(angle_min - angle_h)
    if angle_diff > 180:
        return round(360 - angle_diff, 1)
    else:
        return  round(angle_diff, 1)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"