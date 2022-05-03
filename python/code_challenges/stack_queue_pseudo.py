from data_structures.stack import Stack
from data_structures.linked_list import TargetError


class PseudoQueue:

    def __init__(self):
        self.inny = Stack()
        self.outty = Stack()

    def enqueue(self, value):
        self.inny.push(value)


    def dequeue(self):
        if self.inny.is_empty(): # if empty raise error
            raise TargetError
        while not self.inny.is_empty(): # if first stack not empty
            pop_back = self.inny.pop() # pop items from inny
            self.outty.push(pop_back) # push it to outty
        outty_item= self.outty.pop() # if inny empty return pop outty item
        while not self.outty.is_empty(): # if outty not empty
            pop_in = self.outty.pop() # pop outty value
            self.inny.push(pop_in) # push it to inny
        return outty_item # if outty empty return pushed items from inny to outty
