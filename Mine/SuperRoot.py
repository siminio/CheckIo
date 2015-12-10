def super_root(number):
    '''
        Returns the super root of a number
        (+/- 0.001).
    '''
    root1 = 1
    root2 = 10
    root = (root1 + root2) / 2
    while abs(root ** root - number) > 0.001:
        if root ** root > number:
            root2 = root
        else:
            root1 = root
        root = (root1 + root2) / 2

    return root

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def check_result(function, number):
        result = function(number)
        if not isinstance(result, (int, float)):
            print("The result should be a float or an integer.")
            return False
        p = result ** result
        if number - 0.001 < p < number + 0.001:
            return True
        return False
    assert check_result(super_root, 4), "Square"
    assert check_result(super_root, 9), "Cube"
    assert check_result(super_root, 81), "Eighty one"
