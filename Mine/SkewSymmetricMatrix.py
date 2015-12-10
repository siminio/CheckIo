def checkio(matrix):
    '''
        Returns True if the matrix
        is a skew-symmetric matrix.
    '''
    matrix_transpose = [list(x) for x in zip(*matrix)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != -matrix_transpose[i][j]:
                return False
    return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-2, -1, 0]]) == True, "1st example"
    assert checkio([
        [0, 1, 2],
        [-1, 1, 1],
        [-2, -1, 0]]) == False, "2nd example"
    assert checkio([
        [0, 1, 2],
        [-1, 0, 1],
        [-3, -1, 0]]) == False, "3rd example"