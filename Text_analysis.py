import string

# print(string.punctuation)

sherlock = (open('sherlock_holmes.txt'))

def skip_gutenberg_header(book):
    header = 1000000
    for i, line in enumerate(book):
        if line.startswith('Produced'):
            header = i
        if i > header:
            print(line)


def total_words(book):
    wordcount = {}
    for word in book.read().split():
        word = word.lower()
        word = word.strip(string.punctuation)
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
    return wordcount


def unique_words(book):
    return len(total_words(book))


def print_most_common(book):
    words = total_words(book)
    sorted_words = sorted(words, key=words.get, reverse=True)
    for item in (sorted_words[0:20]):
        print("{0:5}:{1:5}".format(item, words[item]))


def print_least_common(book):
    words = total_words(book)
    sorted_words = sorted(words, key=words.get, reverse=False)
    for item in (sorted_words[0:20]):
        print("{0:20}:{1:5}".format(item, words[item]))

