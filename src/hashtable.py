# '''
# Linked List hash table key/value pair
# '''
import hashlib
import bcrypt

# Forgot to make a separate branch again.


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        """
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            pair = self.storage[index]
            finished = False

            while pair is not None and not finished:
                if pair.key is key:
                    pair.value = value
                    finished = True
                elif pair.next is None:
                    pair.next = LinkedPair(key, value)
                    found = True
                else:
                    pair = pair.next

        else:
            self.storage[index] = LinkedPair(key, value)

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """

        index = self._hash_mod(key)

        if self.storage[index] is None:
            print(f"The index {index} was not found.")
            return

        # Something is going wrong in this method.
        self.storage[index] = None

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        # index = self._hash_mod(key)
        # if self.storage[index] not in self.storage:
        #     return None
        # else:
        #     return self.storage[index]
        # return self.storage[index].value

        # index = self._hash_mod(key)
        # pair = self.storage[index]

        # if pair is None:
        #     return None
        # else:
        #     return pair.value

        index = self._hash_mod(key)
        pair = self.storage[index]

        if pair is not None:
            current_pair = self.storage[index]

            while current_pair is not None:
                if current_pair.key is key:
                    return current_pair.value
                else:
                    current_pair = current_pair.next

            else:
                return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        # self.capacity *= 2
        # new_storage = [None] * self.capacity
        # for i in range(len(self.storage)):
        #     new_storage[i] = self.storage[i]

        # self.storage = new_storage

        self.capacity *= 2
        new_storage = [None] * self.capacity

        for pair in self.storage:
            if pair is not None:
                new_index = self._hash_mod(pair.key)
                new_storage[new_index] = pair

        self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
