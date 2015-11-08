# -*- coding: utf-8 *-*

def count_neighbours(data, pos_x, pos_y):
    '''
        Takes an array and the position of a cell and 
        returns the number of neightboors of this cell.
    '''
    vector = [-1, 0, 1]
    count = 0
    #Create all combinations possible
    for vect_x in vector:
        for vect_y in vector:
            #Do not count the starting cell as a neightboor
            if vect_x != 0 or vect_y != 0:
                new_posx = pos_x + vect_x
                new_posy = pos_y + vect_y
                #Check if it is a valid cell
                if new_posx >= 0 and new_posy >= 0 and new_posx < len(data) and new_posy < len(data[0]):
                    if data[new_posx][new_posy] == 1:
                        count += 1
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
