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
    for letter in word:
        if letter not in available:
            return False
        return True


print('\nAvoids')
print(uses_only('Babson', 'aBbsonxyz'))
print(uses_only('college', 'aBbsonxyz'))


def uses_all(word, required):
    """
    takes a word and a string of required letters, and that returns True if
    the word uses all the required letters at least once.
    """
    for letter in required:
        if letter not in word:
            return False
    return True

print('\nuses_all')
print(uses_all('Babson', 'abs'))
print(uses_all('college', 'abs'))


def is_abecedarian(word):
    """
    returns True if the letters in a word appear in alphabetical order
    (double letters are ok).
    """
    last_letter = word[0]
    for letter in word:
        if letter < last_letter:
            return False
        last_letter = letter
    return True

print('\nabecedarian')
print(is_abecedarian('abs'))
print(is_abecedarian('college'))

# Exercise 2
a = 'apple'
def is_abecedarian_recursion(word):
    # print(word)
    if len(word) == 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian_recursion(word[1:])

print('\nabecedarian recursion')
print(is_abecedarian_recursion('abs'))
print(is_abecedarian_recursion('college'))

def is_abecedarian_while(word):
    i = 0
    while i < len(word)-1:
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True

print('\nabecedarian while')
print(is_abecedarian_while('abs'))
print(is_abecedarian_while('college'))

# Exercise 3
def is_triple_double(word):
    i = 0
    count = 0
    # this loop goes through each letter. the while loop will stop once you get to the last letter
    # count keeps track of how many doubles there have been so far in a row
    while i < len(word)-1:
        print(word[i])
        if word[i] == word[i+1]:
            count += 1
            if count == 3:
                return True
            i += 2
        else:
            count = 0
            i += 1
    return False



print(is_triple_double('dork'))

