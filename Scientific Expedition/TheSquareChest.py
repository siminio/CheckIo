# -*- coding: utf-8 *-*

def checkio(lines_list):
    """
        Returns the quantity of squares.
    """
    for i in range(len(lines_list)):
        if lines_list[i][0] > lines_list[i][1]:
            lines_list[i] = [lines_list[i][1], lines_list[i][0]]
    l = 4
    count_squares = 0
    for i in range(16):
        for a in range(1, 4):
            is_square = True
            for offset in range(a):
                if [i+offset, i + offset + 1] not in lines_list:
                    is_square = False
                if [i + offset * l, i + l * (offset + 1)] not in lines_list:
                    is_square = False
                if [i + a + offset * l, i + a + l * (offset + 1)] not in lines_list:
                    is_square = False
                if [i + (a * l) + offset, i + (a * l) + offset +1] not in lines_list:
                    is_square = False
            if is_square:
                count_squares += 1
    return count_squares


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"