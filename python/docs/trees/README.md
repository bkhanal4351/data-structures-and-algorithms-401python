# Trees
Create two separate classes Binary tree and Binary search tree to implement features described in Challene.

## Challenge
Create a Binary Tree class
Define a method for each of the depth first traversals:
pre order
in order
post order which returns an array of the values, ordered appropriately.
Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

Binary Search Tree
Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
Add
Arguments: value
Return: nothing
Adds a new node with that value in the correct location in the binary search tree.
Contains
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
Create a Binary tree class with three methods to perform pre-order, in-order and post-order.
  1. pre-order- created pre-mrthod which performs the search root-> left->right
  2. in_order : performs left->root->right
  3. post_order: performs left->right->root
Create a Binary search tree class to perform add, contains.
add: if the the value is grater than root value go right else go left
contains: if value is greater than root value search right else left

Big 0:
time: is O(n) , from my understanding, it seems like the operations only goes through the iterations once and optimizing with higher number to right and lower to left minimizes the time complexity,
Space is constant it only holds value temporarily,

## API
As per description, I do not think I am using any of the publicy available methods.
