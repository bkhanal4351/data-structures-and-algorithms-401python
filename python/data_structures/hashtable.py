from data_structures.linked_list import LinkedList

class Hashtable:
    """
    Put docstring here
    """

    def __init__(self, size=1024, key=None):
        self.size = size
        self.buckets = [None] * self.size
        self.key = key

    def hash(self, key):
        char_sum = 0
        for char in key:
            char_sum += ord(char)
        primed = char_sum * 599
        index = primed % self.size
        return index

    def set(self, key, value):
        index = self.hash(key)
        if not self.buckets[index]:
            self.buckets[index] = LinkedList()
        bucket = self.buckets[index]
        bucket.insert((key, value))

        return None

    def get(self, key):
        index = self.hash(key)
        if self.buckets[index] is None:
            return None
        bucket = self.buckets[index]
        current = bucket.head
        while current:
            pair = current.value
            current_key = pair[0]
            if current_key == key:
                return pair[1]

            current = current.next



    def contains(self, key):
        return bool(self.get(key))

    def keys(self):
        all_keys = set()

        for bucket in self.buckets:
            if bucket is not None:
                current = bucket.head
                while current:
                    pair = current.value
                    current_key = pair[0]
                    all_keys.add(current_key)
                    current = current.next
        return all_keys

