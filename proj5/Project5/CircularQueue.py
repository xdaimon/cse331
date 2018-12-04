"""
This module implements a circular queue
"""

class CircularQueue():
    """This is a circular queue class"""
    # DO NOT MODIFY THESE METHODS
    def __init__(self, capacity=4):
        """
        Initialize the queue with an initial capacity
        :param capacity: the initial capacity of the queue
        """
        self.capacity = capacity
        self.size = 0
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0


    def __eq__(self, other):
        """
        Defines equality for two queues
        :return: true if two queues are equal, false otherwise
        """
        if self.capacity != other.capacity:
            return False
        for i in range(self.capacity):
            if self.data[i] != other.data[i]:
                return False
        return self.head == other.head and self.tail == other.tail and self.size == other.size

    # -----------MODIFY BELOW--------------

    def __str__(self):
        """Return a canonical str representation of the objet"""
        str_rep = '\n'
        str_rep += 'Capacity: ' + str(self.capacity) + '\n'
        str_rep += 'Size: ' + str(self.size) + '\n'
        str_rep += 'Data: ' + str(self.data) + '\n'
        str_rep += 'Head: ' + str(self.head) + '\n'
        str_rep += 'Tail: ' + str(self.tail) + '\n'
        return str_rep

    def is_empty(self):
        # lecture slides give
        # is_empty = front == rear
        # but if front == rear then how do we know if we are full or if we are
        # empty?
        # i mean it's easily fixed by keeping the invariant that we are never
        # full.
        return self.size == 0

    def __len__(self):
        """Return the number of elements in the circular queue"""
        # lecture slides give
        # len = (n - (front - rear)) % n
        # this shit has issues ^^^ when rear is a one past pointer and the
        # queue is completely full
        return self.size

    def first_value(self):
        """
        Return the value at the front of the queue if the queue is not empty
        otherwise return None
        """
        if not self.is_empty():
            return self.data[self.head]

    def enqueue(self, val):
        """Place a value at the back of the queue
        :param val: the value to put into the queue
        :return: None, for your convenience
        """
        self.data[self.tail] = val
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1
        if self.size >= self.capacity:
            self.grow()
        return None

    def dequeue(self):
        """
        Remove and return the element at the front of the queue if the queue
        is not empty, otherwise returns None
        :return val: the value that was at the front of the queue
        """
        if self.is_empty():
            return None
        val = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        if self.size <= self.capacity // 4:
            self.shrink()
        return val

    def refit(self, new_capacity):
        """Update the storage of the queue to have capacity = new_capacity"""
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[(self.head + i) % self.capacity]
        self.capacity = new_capacity
        self.data = new_data
        self.head = 0
        self.tail = self.size

    def grow(self):
        """Doubles the size of the underlying storage"""
        self.refit(max(self.capacity * 2, 4))

    def shrink(self):
        """
        Halves the size of the underlying storage unless half of the storage
        size is less than 4
        """
        if self.capacity // 2 < 4:
            return
        self.refit(self.capacity // 2)

