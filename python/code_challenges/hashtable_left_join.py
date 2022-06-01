
'''
left join = grab all from left and intersection of left and right.
'''


def left_join(left_table, right_table):
    output = [] # create an empty list
    for key in left_table: # since we are doing left join, grab key from left hash/table
        join_left = [key, left_table.get(key), right_table.get(key)or "NONE"] # for each item in left assign join_left variable with key, value in left and value in right table(if the same key exist in the left). get() returns the value of the item with provided key
        output.append(join_left) # append the outcome to empty list
    return output # return output


