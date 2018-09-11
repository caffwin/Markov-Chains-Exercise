"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here

    text_file = open(file_path)
    text = text_file.read()
    # text = text.replace("\n"," ")

    return text


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    words = text_string.split()

    chains = {}

    # i = 0
    for i in range(len(words) - 2):
    # while i < len(words) - 2:
        
        new_ngram = (words[i], words[i+1])

        # could do this in one line with a .get() statement *TRY LATER*
        if new_ngram in chains:
            chains[new_ngram].append(words[i+2]) #appends new value to existing value list for given key
        else: #else happens first
            chains[new_ngram] = [words[i+2]] #assigns new key to value 

        # i += 1

    return chains


def make_text(chains):
    """Return text from chains."""
    # create sorted list of keys from dictionary
    # return random key to get our first key

    # create chain of fake text with link
    # randomly pick key and value


    words = []

    keys_list = sorted(chains) # makes chains into a list and sorts alphabetically

    first_key = choice(keys_list) #assigns first key to random value in keys_list
    words = list(first_key) # Creates a new list called words and assigns it to values in tuple first_key

    key = first_key

    while key:
        if key in chains:
            next_word = choice(chains[key])
            words.append(next_word)
            next_key = (key[1], next_word)
            key = next_key
        else:
            break



    # your code goes here

    return " ".join(words)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
