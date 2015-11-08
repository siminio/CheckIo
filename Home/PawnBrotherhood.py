# -*- coding: utf-8 *-*

def convert_str_to_pos(str_pawn):
    '''
        Converts a position like "b4" or "c3"
        in a position like (2, 4) or (3, 3)
    '''        
    return (ord(str_pawn[0]) - ord('a') + 1, int(str_pawn[1]))

def safe_pawns(pawns):
    '''
        Returns the number of pawns that are safe.
    '''
    set_pawns = set()
    safe_pos = set()
    vects = [[1, 1], [-1, 1]]

    for pawn in pawns:
        set_pawns.add(convert_str_to_pos(pawn))
    for pawn in set_pawns:
        for vect in vects:
            safe_pos.add((pawn[0] + vect[0], pawn[1] + vect[1]))
    return len(set_pawns.intersection(safe_pos))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1