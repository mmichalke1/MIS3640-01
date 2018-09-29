fin = open('words.txt')

def read_long_words(list):
    """
    prints only the words with more than 20 characters
    """
    for line in list:
        word = line.strip()
        if len(word) > 20:
            print(word)

read_long_words(fin)


def has_no_e(word):
    """
    returns True if the given word doesn’t have the letter “e” in it.
    """
    if 'e' in word or 'E' in word:
        return False
    else:
        return True

print('has no e')
print(has_no_e('Babson'))
print(has_no_e('College'))


def avoids(word, forbidden):
    """
    takes a word and a string of forbidden letters, and that returns True
    if the word doesn’t use any of the forbidden letters.
    """
    for letter in forbidden:
        if letter in word:
            return False
    return True

print('\nAvoids')
print(avoids('Babson', 'ab'))
print(avoids('College', 'ab'))
print(avoids('Babson', 'lmk'))


def uses_only(word, available):
    """
    takes a word and a string of letters, and that returns True if the word
    contains only letters in the list.
    """
    pass


print(uses_only('Babson', 'aBbsonxyz'))
print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    pass


print(uses_all('Babson', 'abs'))
print(uses_all('college', 'abs'))


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    pass


print(is_abecedarian('abs'))
print(is_abecedarian('college'))
