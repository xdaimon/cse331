"""
# Project 4
# Name: Bradley Bauer
# PID: A56677986
"""

class Stack:
    """
    Stack class
    """
    def __init__(self, capacity=2):
        """
        DO NOT MODIFY
        Creates an empty Stack with a fixed capacity
        :param capacity: Initial size of the stack. Default size 2.
        """
        self.capacity = capacity
        self.data = [None] * self.capacity
        self.size = 0

    def __str__(self):
        """
        DO NOT MODIFY
        Prints the values in the stack from bottom to top. Then, prints capacity.
        :return: string
        """
        if self.size == 0:
            return "Empty Stack"

        output = []
        for i in range(self.size):
            output.append(str(self.data[i]))
        return "{} Capacity: {}".format(output, str(self.capacity))

    def __eq__(self, stack2):
        """
        DO NOT MODIFY
        Checks if two stacks are equivalent to each other. Checks equivalency of data and capacity
        :return: True if equal, False if not
        """
        if self.capacity != stack2.capacity:
            return False

        count = 0
        for item in self.data:
            if item != stack2.data[count]:
                return False
            count += 1

        return True

    def stack_size(self):
        """Returns the current number of items in the stack."""
        return self.size

    def is_empty(self):
        """Returns True if the stack is empty, False if not."""
        return self.size == 0

    def top(self):
        """Returns the top item from the stack, None if the stack is empty. Does NOT remove the top item."""
        if self.is_empty():
            return None
        return self.data[self.size - 1]

    def push(self, val):
        """
        Put an item on top of the stack
        :param val: the value to place on the stack
        """
        if self.size >= self.capacity:
            self.grow()
        self.data[self.size] = val
        self.size += 1

    def pop(self):
        """
        Pop an item off the top of the stack
        Returns the popped item
        """
        if self.is_empty():
            return None

        self.size -= 1
        ret = self.data[self.size]
        self.data[self.size] = None

        if self.size <= self.capacity // 2:
            self.shrink()

        return ret

    def grow(self):
        """Double the size of the stack"""
        if self.capacity <= 2:
            self.capacity = 2
        self.data.extend([None]*self.capacity)
        self.capacity *= 2

    def shrink(self):
        """Halve the size of the stack"""
        self.capacity //= 2
        if self.capacity <= 2:
            self.capacity = 2
        del self.data[self.capacity:]

def reverse(stack):
    """
    Reverse the order of the given stack
    Returns the reversed stack
    """
    ret_stack = Stack(stack.stack_size())
    for i in range(stack.stack_size()):
        ret_stack.push(stack.pop())
    return ret_stack

def replace(stack, old, new):
    """
    Replace all values in stack that equal old with value of new
    Returns the stack with the replacements
    """
    ret_stack = Stack(stack.stack_size())
    for i in range(stack.stack_size()):
        top = stack.pop()
        if top == old:
            top = new
        ret_stack.push(top)
    return reverse(ret_stack)

