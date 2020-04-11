def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    count = 0
    for i, num in enumerate(sequence):
        for num2 in sequence[i:]:
            if num > num2:
                count += 1
    return count
