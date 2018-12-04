class HashNode:
    """
    DO NOT EDIT
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __repr__(self):
        return f"HashNode({self.key}, {self.value})"

class HashTable:
    """
    Hash table class, utilizes double hashing for conflicts
    """

    def __init__(self, capacity=4):
        """
        DO NOT EDIT
        Initializes hash table
        :param tableSize: size of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None]*capacity

    def __eq__(self, other):
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __repr__(self):
        pass

    def hash_function(self, x):
        """
        ---DO NOT EDIT---

        Converts a string x into a bin number for our hash table
        :param x: key to be hashed
        :return: bin number to insert hash item at in our table, -1 if x is an empty string
        """
        if not x:
            return -1
        hashed_value = 0

        for char in x:
            hashed_value = 181 * hashed_value + ord(char)

        return hashed_value % self.capacity

    def insert(self, key, value):
        """
        Inserts HashNode into the HashTable
        Does nothing if key is empty
        :param key: the key of the node to insert
        :param value: the value of the node to insert
        :return: None
        """
        if not key:
            return
        i = self.quadratic_probe(key)
        if self.table[i] is None:
            self.table[i] = HashNode(key, value)
            self.size += 1
        else:
            self.table[i].value = value
        if self.size / self.capacity > 0.75:
            self.grow()

    def quadratic_probe(self, key):
        """
        Returns the table index of key if key is in the table
        Assumes table.capacity > 0 and load factor < 1
        :param key: the key of the node to search for
        :return: an index i with table[i].key == key or table[i] == None
        """
        if not key:
            return -1
        # # show that for capacity in [4, 2**8) we have that
        # #   if capacity is a power of two, then our quadratic probe function
        # #   visits every index in the table for some number of
        # #   probes less than 2 * capacity
        # def is_pow2(x):
        #     return 2**m.ceil(m.log2(x)) == capacity
        # for capacity in range(4, 2**8):     # for all possible capacities
        #     for hash in range(capacity):    # for all possible initial hashes
        #         ls = set()
        #         hash %= capacity
        #         for i in range(2*capacity): # show that every index is visited
        #             hash = (hash + i**2) % capacity
        #             ls.add(hash)
        #         if len(ls) != capacity and is_pow2(capacity): # if cap is pow2
        #             print(ls)
        #
        # if self.capacity is a power of two and we maintain the loadfactor
        # <= .75 invariant then there is always a none value in the table and we
        # will always find atleast one index with self.table[i] == None in the
        # below loop, thus we never return None
        next_avail = None
        buckets_probed = 0
        i = self.hash_function(key)
        while (self.table[i] is None or self.table[i].key != key) and buckets_probed < 2 * self.capacity:
            if next_avail is None and self.table[i] is None:
                next_avail = i
            i = (i + buckets_probed**2) % self.capacity
            buckets_probed += 1
        if self.table[i] is None or self.table[i].key != key: # did not find key
            return next_avail
        if self.table[i].key == key:
            return i

    def find(self, key):
        """
        Searches the hash table for a node with node.key == key
        :return: False or the node with node.key == key
        """
        i = self.quadratic_probe(key)
        if self.table[i] is None or self.table[i].key != key:
            return False
        if self.table[i].key == key:
            return self.table[i]

    def lookup(self, key):
        """
        Searches the hash table for a node with node.key == key
        :return: None or the value of the node with node.key == key
        """
        exists = self.find(key)
        return exists and exists.value

    def delete(self, key):
        """
        Deletes the key in the hash table by setting self.table[i] to None
        :param key: the key of the node to remove from the hash table
        :return: None
        """
        i = self.quadratic_probe(key)
        if self.table[i] is None:
            return
        self.table[i] = None
        self.size -= 1

    def grow(self):
        """
        Doubles the capacity of the hash table in O(n) time
        :return: None
        """
        self.capacity *= 2
        self.rehash()

    def rehash(self):
        """
        Rehashes all items inside of the table in O(n) time
        However, if all items in the table have the same hash then the kth call
        to insert will cost O(k) time. So the cost of rehash when all items have
        the same hash is 1 + 2 + 3 + 4 + ... + n = O(n^2)
        :return: None
        """
        old_table = self.table
        self.size = 0
        self.table = [None] * self.capacity
        for node in old_table:
            if not node:
                continue
            self.insert(node.key, node.value)

def string_difference(string1, string2):
    """
    if string1 contains n a's, p b's, and i c's
    and string2 contains m a's, q b's, and j c's
    then this function returns the set {a^abs(n-m), b^abs(p-q), c^abs(i-j)}
    where a^n = 'a'*n in python and a^0 is not included in the returned set
    :param string1: first input string to algorithm
    :param string2: second input string to algorithm
    :return ret_set: set containing char^abs(pow diff) for each char in input
    strings
    """
    hash_table = HashTable()
    # count powers on chars in string1
    for char in string1:
        count = hash_table.lookup(char)
        hash_table.insert(char, 1 + int(count))
    # compute power difference
    for char in string2:
        count = hash_table.lookup(char)
        hash_table.insert(char, -1 + int(count))
    # create the return set
    ret_set = set()
    for node in hash_table.table:
        if not node:
            continue
        char, count = node.key, node.value
        if not count:
            continue
        ret_set.add(char * abs(count))
    return ret_set

