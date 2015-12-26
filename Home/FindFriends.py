# -*- coding: utf-8 *-*

def check_connection(network, first, second):
    '''
        Returns True if first and second
        are friends or have friends in common.
    '''
    friends = set([first,])
    init_len_friends = 1
    new_len_friends = 0
    while new_len_friends != init_len_friends:
        init_len_friends = len(friends)
        for pair in network:
            person1, person2 = pair.split('-')
            if person1 in friends or person2 in friends:
                friends.update({person1, person2})
        new_len_friends = len(friends)
    if second in friends:
        return True
    else:
        return False



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
