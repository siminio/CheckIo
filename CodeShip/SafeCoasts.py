# -*- coding: utf-8 *-*

vects_diago = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
vects_sides = [[-1, 0], [1, 0], [0, -1], [0, 1]]
vects_all = vects_diago + vects_sides

def paint_recifs(regional_map):
    '''
        Takes an incomplete map as input
        and returns the map with the safe cells.
        All cells next to land are safe (including
        cells at the diagonals).
    '''
    for i in range(len(regional_map)):
        for j in range(len(regional_map[0])):
            for vect in vects_all:
                new_pos = [i + vect[0], j + vect[1]]
                if new_pos[0] < 0 or new_pos[0] >= len(regional_map):
                    continue
                if new_pos[1] < 0 or new_pos[1] >= len(regional_map[0]):
                    continue
                if regional_map[new_pos[0]][new_pos[1]] == 'X' and regional_map[i][j] == '.':
                    regional_map[i][j] = 'S'

def paint_ghosts(regional_map):
    '''
        Paint all cells where the ghost ship can go.
        The ghost ship can move to neighbour cells at
        in the cardinal directions - up, down, left, and right.
    '''
    is_added = True
    # As long as new cells are added, we continue
    while is_added:
        is_added = False
        for i in range(len(regional_map)):
            for j in range(len(regional_map[0])):
                for vect in vects_sides:
                    new_pos = [i + vect[0], j + vect[1]]
                    if new_pos[0] < 0 or new_pos[0] >= len(regional_map):
                        continue
                    if new_pos[1] < 0 or new_pos[1] >= len(regional_map[0]):
                        continue
                    if regional_map[new_pos[0]][new_pos[1]] == 'D':
                        if regional_map[i][j] == '.':
                            regional_map[i][j] = 'D'
                            is_added = True


def finish_map(regional_map):
    '''
        Takes an incomplete map as input
        and returns the completed map.
        Cells where the Ghost Ship can appear are
        marked with a "D"
        Cells which are land are marked with a "X"
        Cells which are safe are marked with a "S"
    '''
    regional_map = list(regional_map)
    for i in range(len(regional_map)):
        regional_map[i] = list(regional_map[i])

    # First Mark all cells next to land as safe
    paint_recifs(regional_map)
    # Second mark cells where the ghost ship can go
    paint_ghosts(regional_map)
    # Finally, mark all other undetermined cells as safe
    for i in range(len(regional_map)):
        for j in range(len(regional_map[0])):
            if regional_map[i][j] == '.':
                regional_map[i][j] = 'S'
    for i in range(len(regional_map)):
        regional_map[i] = ''.join(regional_map[i])
    return regional_map


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(finish_map(("D..", "...", "...")), (list, tuple)), "List or tuple"
    assert list(finish_map(("D..XX.....",
                            "...X......",
                            ".......X..",
                            ".......X..",
                            "...X...X..",
                            "...XXXXX..",
                            "X.........",
                            "..X.......",
                            "..........",
                            "D...X....D"))) == ["DDSXXSDDDD",
                                                "DDSXSSSSSD",
                                                "DDSSSSSXSD",
                                                "DDSSSSSXSD",
                                                "DDSXSSSXSD",
                                                "SSSXXXXXSD",
                                                "XSSSSSSSSD",
                                                "SSXSDDDDDD",
                                                "DSSSSSDDDD",
                                                "DDDSXSDDDD"], "Example"
    assert list(finish_map(("........",
                            "........",
                            "X.X..X.X",
                            "........",
                            "...D....",
                            "........",
                            "X.X..X.X",
                            "........",
                            "........",))) == ["SSSSSSSS",
                                               "SSSSSSSS",
                                               "XSXSSXSX",
                                               "SSSSSSSS",
                                               "DDDDDDDD",
                                               "SSSSSSSS",
                                               'XSXSSXSX',
                                               "SSSSSSSS",
                                               "SSSSSSSS"], "Walls"