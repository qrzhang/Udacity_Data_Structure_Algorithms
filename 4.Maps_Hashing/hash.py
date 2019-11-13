"""
Load Factor = Number of Entries / Number of Buckets
The purpose of a load factor is to give us a sense of how "full" a hash table is.

On the flip side, the closer our load factor is to 1 (meaning the number of values
equals the number of buckets), the better it would be for us to rehash and add more
buckets. Any table with a load value greater than 1 is guaranteed to have collisions.
"""

# A python dictionary is a hash map!

"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def my_store(self, string):
        """Input a string that's stored in
        the table."""
        i = 0
        while self.table[i]:
            i += 1
        self.table[i] = string

    def store(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] is not None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def my_lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        i = 0
        while self.table[i]:
            if self.table[i] == string:
                return self.calculate_hash_value(string)
            i += 1
        return -1

    def lookup(self, string):
        hv = self.calculate_hash_value(string)
        if hv != -1:
            if self.table[hv] is not None:
                if string in self.table[hv]:
                    return hv
        return -1

    def my_calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        if len(string) > 1:
            return ord(string[0]) * 100 + ord(string[1])
        else:
            return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
