# Challenge Summary
Write a function called repeated word that finds the first word to occur more than once in a string
  - Arguments: string
  - Return: string


## Whiteboard Process
1[](hashmap-repeated-word.png)

## Approach & Efficiency
-  Write a function with argument string
-  set a variable with empty set
-  using regex filter out only the word characters
-  lowercase all word chars and split them
-  go through for loop for each word in the stripped string
-  if word is in the set return the word
-  if word is not present add the word to the set

Big 0
- Time: O(n): Since we are only iterating through the string until we find a matching word. However, if no matching word is - there then it is O(N).
Space:O(1): Since we are only saving the first repeated word.

## Solution
import re

def first_repeated_word(string):
    unique_word = set() # store in a set becuase set does is mutable , iterable and does not allow duplicate values
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
