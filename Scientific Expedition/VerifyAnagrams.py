from collections import Counter

def verify_anagrams(first_word, second_word):
    '''
        Returns True if the second word
        is the anagram of the first word.
    '''
    #Dictionnary where the letters of the first word are counted
    dict_num_letters = Counter()
    for c in first_word:
        dict_num_letters[c.lower()] += 1
    #Substracts the letters of the second word    
    for c in second_word:
        dict_num_letters[c.lower()] -= 1
    #If there is a difference then it is not an anagram
    for k in dict_num_letters.keys():
        if dict_num_letters[k] != 0 and k != ' ':
            return False
    return True

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"

