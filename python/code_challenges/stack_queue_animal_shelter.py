from data_structures.queue import Queue



class AnimalShelter: # creating instance of Animal Shelter
    def __init__(self):
        self.cat = Queue() # instance of Queue is assigned to self.cat
        # cat.speices = 'cat'
        self.dog = Queue()

    def enqueue(self, animal): # enqueueing cat. animal.speices = cat.speices = cat
        if animal.speices == 'cat': # if input is string of cat = 'cat'
            self.cat.enqueue(animal) # add to the stack

        elif animal.speices == 'dog':
            self.dog.enqueue(animal)

    def dequeue(self, user_pick):
        if user_pick is 'cat': # if choice is cat then return dequeue of self.cat
            return self.cat.dequeue()
        elif user_pick is 'dog':
            return self.dog.dequeue()

        return None # if neither dog or cat return None


class Dog:
    def __init__(self, speices='dog'):
        self.speices = speices


class Cat:
    def __init__(self, speices='cat'): # creating instance of Cat with speices equals to cat
        self.speices = speices
