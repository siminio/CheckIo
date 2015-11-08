# -*- coding: utf-8 *-*

def checkio(data):
    '''
        Takes a grid representing a tic-tac-toe game
        and returns the winner
        ("X" : X wins
         "O" : O wins
         "D" : Draw)
    '''
    winner = 'D'
    #Check horizontal lines
    for i in range(3):
        if data[i] == 'XXX':
            winner = 'X'
        if data[i] == 'OOO':
            winner = 'O'
    #Check vertical lines
    for i in range(3):
        if data[0][i] == data[1][i] == data[2][i] == 'X':
            winner = 'X'
        if data[0][i] == data[1][i] == data[2][i] == 'O':
            winner = 'O'

    #Chek diagonals
    if data[0][0] == data[1][1] == data[2][2] == 'X' or data[2][0] == data[1][1] == data[0][2] == 'X':
            winner = 'X'
    if data[0][0] == data[1][1] == data[2][2] == 'O' or data[2][0] == data[1][1] == data[0][2] == 'O':
            winner = 'O'
            
    return winner

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"