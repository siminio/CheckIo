def can_pass(matrix, first, second):
    '''
        Returns True if there is a path
        between first and second otherwise
        returns False.
    '''
    vects = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = [first,]
    list_processed_nodes = []
    # Each cell having the same value as the variable value is a cell where you can move at
    value = matrix[first[0]][first[1]]
    while queue != []:
        node = queue[0]
        # Path found
        if node[0] == second[0] and node[1] == second[1]:
            return True
        else:
            for vect in vects:
                row = node[0] + vect[0]
                col = node[1] + vect[1]
                if row < 0 or row >= len(matrix):
                    continue
                if col < 0 or col >= len(matrix[0]):
                    continue
                if matrix[row][col] == value and [row, col] not in list_processed_nodes:
                    queue.append([row, col])
                    list_processed_nodes.append([row, col])
            # Removes from the queue the element that has been processed
            queue.pop(0)
    # If after checking all cells, we don't find the cell second then there is no path
    # between first and second.
    return False


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
