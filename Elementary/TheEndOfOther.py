# -*- coding: utf-8 *-*

def checkio(words_set):
    """
        Returns True if one word in the set of words is the end of another word
        in the set.
    """
    for word1 in words_set:
        for word2 in words_set:
            if word1 != word2 and word1 in word2:
                if word1 == word2[-len(word1):]:
                    return True
    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"