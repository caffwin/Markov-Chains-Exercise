"""Generate Markov text from text files."""

from random import choice
import sys
import string

#constant - how many words in "gram"
N = 3


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


def make_chains(input_texts):
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

    chains = {}

    # print(len(locals()))
    # print(len(args))

    for i in range(len(input_texts)):

        text_string = input_texts[i]

        words = text_string.split()

    # # i = 0
    # for i in range(len(words) - 2):
    # # while i < len(words) - 2:
        
    #     new_ngram = (words[i], words[i+1])

    #     # could do this in one line with a .get() statement *TRY LATER*
    #     if new_ngram in chains:
    #         chains[new_ngram].append(words[i+2]) #appends new value to existing value list for given key
    #     else: #else happens first
    #         chains[new_ngram] = [words[i+2]] #assigns new key to value 

    #     # i += 1

    # return chains

        for i in range(len(words) - N): #looping through each string in a list up to len - N
            
            new_ngram_list = [] # creating a new list 
            for j in range(N): # loops N times
                new_ngram_list.append(words[i+j]) # Adding words and i + j index to new_ngram_list

            new_ngram = tuple(new_ngram_list)

            # could do this in one line with a .get() statement *TRY LATER*
            if new_ngram in chains:
                chains[new_ngram].append(words[i+N]) #appends new value to existing value list for given key
            else: #else happens first
                chains[new_ngram] = [words[i+N]] #assigns new key to value 
    
    return chains



def make_text(chains):
    """Return text from chains."""
    # create sorted list of keys from dictionary
    # return random key to get our first key

    # create chain of fake text with link
    # randomly pick key and value


    words = []

    keys_list = sorted(chains) # makes chains into a list and sorts alphabetically

    # first_key = choice(keys_list) #assigns first key to random value in keys_list
    # words = list(first_key) # Creates a new list called words and assigns it to values in tuple first_key


    # loop through keys_list, make keys_list_startswithupper

    # loop through len(keys_list) times 
    keys_list_startswithupper = []

    for i in range(len(keys_list)):
        if keys_list[i][0][0].isupper():
            keys_list_startswithupper.append(keys_list[i])

    # print(keys_list_startswithupper)


    first_key = choice(keys_list_startswithupper) #assigns first key to random value in keys_list
    words = list(first_key) # Creates a new list called words and assigns it to values in tuple first_key

    key = first_key # assigns first_key (random value) to key (tuple)

    while key: #while True
        if key in chains: #if we can find the tuple key in chains:
            next_word = choice(chains[key]) # Assign new variable next_word to random value from this key
            words.append(next_word) #Add new_words to list words

            # next_key = (key[1], next_word)
            next_key_list = list(key)[1:]  #Create a new var next_key_list, key as a list from index 1 to last index
            next_key_list.append(next_word) # adds next_word (string) to this list
            next_key = tuple(next_key_list) # creates a variable next_key, a tuple of list next_key_list

            key = next_key # Assigns next_key (tuple) as the key
            # print(key) # This prints each n gram
        else:
            break

    last_char = words[-1][-1]
    while last_char not in string.punctuation:
        words.pop()
        last_char = words[-1][-1] # reassigns last_char to last index of updated list


    # your code goes here
    return " ".join(words)


input_path = sys.argv[1]
input_texts = []

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

for i in range(len(sys.argv)-1):
    input_texts.append(open_and_read_file(sys.argv[i+1]))

chains = make_chains(input_texts)

# try:
#     if sys.argv[2]:
#         input_text2 = open_and_read_file(sys.argv[2])
#         chains = make_chains(input_text, input_text2)
# except IndexError:
#     # Get a Markov chain
#     chains = make_chains(input_text)

# input_ngram = ???

# # Get a Markov chain
# chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
