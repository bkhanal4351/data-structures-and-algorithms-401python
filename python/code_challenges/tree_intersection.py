from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable


# def tree_intersection(bin1, bin2):
#         first_list = [] # create an empty list to store values from first tree
#         second_list = [] # create a second empty list to store values from second tree
#         common_values = [] # create another empty list to store common values
#         bin1 = bin1.in_order() # traverse through first tree
#         bin2 = bin2.in_order() # traverse through second tree

#         for value in bin1: # loop through first list
#                 first_list.append(value) # append values from tree to the empty list
#         for value in bin2:
#                 second_list.append(value)

#         for value in first_list: # check if value in first list exists in second list
#                 if value in second_list:
#                         common_values.append(value) # if common values append to the list


#         return common_values # return common values


def tree_intersection(bin1,bin2):
        common_value = set() # create an empty set so no duplicate values are allowed
        bin1 = bin1.pre_order() # traverse using one of the methods. I used pre_order
        bin2 = bin2.pre_order()
        hashtable = Hashtable() # calling hashtable class
        for value in bin1:
                hashtable.set(str(value), value) # adding values to the set from bin1
        for value in bin2:
                if hashtable.contains(str(value)): # if it contains in bin2 add to the set
                        common_value.add(value)
        return common_value # return set with common values









