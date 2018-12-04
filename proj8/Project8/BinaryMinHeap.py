########################################
# PROJECT: Binary Min Heap and Sort
# Author: Bradley Bauer
########################################

class BinaryMinHeap:
    # DO NOT MODIFY THIS CLASS #
    def __init__(self):
        """
        Creates an empty hash table with a fixed capacity
        """
        self.table = []


    def __eq__(self, other):
        """
        Equality comparison for heaps
        :param other: Heap being compared to
        :return: True if equal, False if not equal
        """
        if len(self.table) != len(other.table):
            return False
        for i in range(len(self.table)):
            if self.table[i] != other.table[i]:
                return False

        return True

    ###### COMPLETE THE FUNCTIONS BELOW ######

    def __str__(self):
        """:return: a string rep of the contents of the min heap"""
        return str(self.table)

    def get_size(self):
        """:return: the number of nodes currently in the heap"""
        return len(self.table)

    def parent(self, position):
        """
        Finds the parent of the node at index position
        :param position: the position of the node described
        :return: the index of the parent noed of the node at position
        """
        return int((position - 1) / 2)

    def left_child(self, position):
        """
        Finds the left child of the node at index position
        :param position: the position of the node to find the child for
        :return: the index of the left child node
        """
        return position * 2 + 1

    def right_child(self, position):
        """
        Finds the right child of the node at index position
        :param position: the position of the node to find the child for
        :return: the index of the right child node
        """
        return position * 2 + 2

    def has_left(self, position):
        """
        Returns whether the node at position has a left child
        :param position: the position of the node to find the child for
        :return: True if the node at index position has a left child, False otherwise
        """
        return self.left_child(position) < self.get_size()

    def has_right(self, position):
        """
        Returns whether the node at position has a right child
        :param position: the position of the node to find the child for
        :return: True if the node at index position has a left child, False otherwise
        """
        return self.right_child(position) < self.get_size()

    def find(self, value):
        """
        Find the inex of the node that has value = value
        :return: an index i with self.table[i] == value or None if no index found
        """
        for i, val in enumerate(self.table):
            if val == value:
                return i

    def heap_push(self, value):
        """
        Adds a node with the given value and adds it to the heap
        Duplicates are ignored
        :param value: value of the node to add to the heap
        :return: None
        """
        if self.find(value) is not None:
            return
        self.table.append(value)
        self.percolate_up(-1)

    def heap_pop(self, value):
        """
        Removes the node with the given value
        :parap value: the value to pop
        :return: None
        """
        index = self.find(value)
        if index is None:
            return
        self.swap(index, -1)
        self.table.pop()
        self.percolate_down(index)

    def pop_min(self):
        """
        Removes the min node in the heap
        :return: the min element in the heap or none if the heap is empty
        """
        sz = self.get_size()
        if not sz:
            return None
        ret = self.table[0]
        self.swap(0, -1)
        self.table.pop()
        self.percolate_down(0)
        return ret

    def swap(self, p1, p2):
        """
        Swaps the elements at indices p1 and p2
        """
        sz = self.get_size()
        if not -sz <= p1 < sz or not -sz <= p2 < sz:
            return
        self.table[p1], self.table[p2] = self.table[p2], self.table[p1]

    def percolate_up(self, position):
        """
        Moves node at index position up the tree until it is in the proper place
        :param position: the position of the node to percolate up
        :return: None
        """
        sz = self.get_size()
        i = position
        if i < 0:
            i += sz
        if not sz or not 0 <= i < sz:
            return
        parent_i = self.parent(i)
        while i != 0:
            if self.table[i] >= self.table[parent_i]:
                return
            self.swap(i, parent_i)
            i = parent_i
            parent_i = self.parent(i)

    def percolate_down(self, position):
        """
        Moves node at index position down the tree until it is in the proper place
        :param position: the position of the node to percolate down
        :return: None
        """
        sz = self.get_size()
        i = position
        if i < 0:
            i += sz
        if not sz or not 0 <= i < sz:
            return
        # tree at i may not be a heap, but left and right subtrees are heaps
        while True:
            left_i = self.left_child(i)
            right_i = self.right_child(i)
            if self.has_left(i) and self.has_right(i):
                left = self.table[left_i]
                right = self.table[right_i]
                if self.table[i] < left and self.table[i] < right:
                    return
                # if table[i] > left but table[i] < right
                # then the heap property is broken and left < right
                # so we should continue moving table[i] down
                min_i = left_i if left < right else right_i
                self.swap(i, min_i)
                i = min_i
            elif self.has_left(i):
                if self.table[i] > self.table[left_i]:
                    self.swap(i, left_i)
                return
            else: # no chidren
                return

def heap_sort(unsorted):
    """
    Given an unsorted list, performs Heap Sort
    :param unsorted: the list to sort
    :return: the sorted list
    """
    n = len(unsorted)
    if n <= 1:
        return unsorted

    # build a heap in O(n)
    # assume left and right subtrees are min heap then do O(height current tree)
    # work to make current tree min heap
    # n/4*2 + n/8*3 + n/16*4 ... = n sum^(lg(n))_2 i/2^i = n * (constant in n)
    # n // 2 - 1 is the last non leaf in the level order traversal
    heap = BinaryMinHeap()
    heap.table = unsorted.copy()
    for i in range(n // 2 - 1, -1, -1):
        heap.percolate_down(i)

    # do O(nlogn) work here since for the first n // 2 pops we do O(h) work
    # since there are n//2 leafs so the height decreases at most 1 during the
    # first n // 2 pop_min() calls.
    ret = [heap.pop_min()]
    for i in range(n - 1):
        ith_min = heap.pop_min()
        if ret[-1] != ith_min:
            ret.append(ith_min)
    return ret
