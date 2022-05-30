# Hashtables
Hastable is a data structure that maps keys to values. In a hash table, data is stored in an array format, where each data value has its own unique index value. Access of data becomes very fast if we know the index of the desired data.

## Challenge
Features
  - Implement a Hashtable Class with the following methods:

1. set
  - Arguments: key, value
  - Returns: nothing
  - This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
  - Should a given key already exist, replace its value from the value argument given to this method.
2. get
  - Arguments: key
  - Returns: Value associated with that key in the table
3. contains
  - Arguments: key
  - Returns: Boolean, indicating if the key exists in the table already.
4. keys
  - Returns: Collection of keys
5. hash
  - Arguments: key
  - Returns: Index in the collection for that key

## Approach & Efficiency
hash table has time and space complecity of O(1)

## API
  - hash : To get the index which is used to place the key.
  - set:to has the key
  - get: returns the value for a given key
  - contains: check and returns bollean if the key is present
  - keys: returns all keys
