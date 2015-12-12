# -*- coding: utf-8 *-*

from string import punctuation

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
LETTER = VOWELS + CONSONANTS

def checkio(text):
    '''
        Return the number of striped words
        (vowels alternating with consonants).
    '''
    text = text.upper()
    # Removing all characters that are not letters
    for c in text:
        if c in punctuation:
            text = text.replace(c, ' ')
    words = text.split(' ')
    total = 0
    for word in words:
        is_striped = True
        if len(word) < 2:
            is_striped = False
            continue
        if word.isalpha() == False:
            is_striped = False
            continue
        for i in range(len(word)-1):
            if word[i] in VOWELS and word[i+1] in VOWELS:
                is_striped = False
                continue
            if word[i] in CONSONANTS and word[i+1] in CONSONANTS:
                is_striped = False
                continue
        if is_striped:
            total += 1
    print(total)
    return total

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"