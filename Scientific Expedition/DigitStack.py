def digit_stack(commands):
    '''
        Function that simulates a stack.
        Returns the result of the successive
        commands.
    '''
    count = 0
    stack = []
    for command in commands:
        if command[:4] == 'PUSH':
            stack.insert(0, int(command[-1]))
        elif command[:4] == 'PEEK':
            if stack != []:
                count += stack[0]
        elif command[:3] == 'POP':
            if stack != []:
                count += stack.pop(0)
    return count

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
