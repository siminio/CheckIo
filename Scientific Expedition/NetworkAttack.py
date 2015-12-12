# -*- coding: utf-8 *-*

def capture(matrix):
    '''
        Time for a virus to capture the whole network.
        Infection starts from the first computer.
        If matrix[i][j] == matrix[j][i] == 1
        then the two computers are directly related.
        The number matrix[i][i] represents the level
        of security.
    '''
    list_infected_nodes = [0]
    dict_safe_nodes = {0:0}
    dict_relations = {}
    for i in range(1, len(matrix)):
        dict_safe_nodes[i] = matrix[i][i]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                if i in dict_relations.keys():
                    dict_relations[i].append(j)
                else:
                    dict_relations[i] = [j]

    time = 0
    while len(list_infected_nodes) != len(matrix):
        time += 1
        list_contaminations = []
        for infected_node in list_infected_nodes:
            for node_to_contaminate in dict_relations[infected_node]:
                if node_to_contaminate not in list_contaminations:
                    dict_safe_nodes[node_to_contaminate] -= 1
                    list_contaminations.append(node_to_contaminate)
        for node in dict_safe_nodes.keys():
            if dict_safe_nodes[node] == 0 and node != 0:
                list_infected_nodes.append(node)
    return time


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
