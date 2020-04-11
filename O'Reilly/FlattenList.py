def flat_list(array):
    """
        Flattens a list.
    """  
    new_list = []
    for elem in array:
        if isinstance(elem,list):
            new_list.extend(flat_list(elem))
        else:
            new_list.append(elem)
    return new_list
