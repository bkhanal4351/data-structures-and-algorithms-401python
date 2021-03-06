# from data_structures.hashtable import Hashtable
import re

def first_repeated_word(string):
    unique_word = set() # store in a set becuase set is mutable , iterable and does not allow duplicate values
    regex = re.compile('[^a-zA-Z ]')
    stripped_string = regex.sub('', string)

    string1 = stripped_string.lower().split()# convert string to lower and split


    for word in string1:
        if word in unique_word:
            # this will end the function and return the repeated word
            return word
        # if word not in set then add the word to the set.
        unique_word.add(word)

    print("no repeated words found") # if no repeated words are found



