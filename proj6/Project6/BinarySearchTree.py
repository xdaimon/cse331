class Node:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class BinarySearchTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True  # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    ### Implement/Modify the functions below ###

    def insert(self, value):
        """
        Insert a value into the binary search tree unless the value is already
        in the tree
        :param value: the value to put into the search tree
        :return node: the node that has been inserted into the tree
        """
        if self.root is None:
            self.root = Node(value)
            self.size += 1
            return self.root

        node = self.search(value, self.root)
        if node is None:
            return None

        if value < node.value:
            node.left = Node(value, node)
            self.size += 1
            return node.left
        if value > node.value:
            node.right = Node(value, node)
            self.size += 1
            return node.right

        # if equal
        return node

    def remove(self, value):
        """
        Remove the node with value from the tree
        :param value: the value to remove from the BST
        :return: None
        """
        if self.root is None:
            return

        # find the node we want to remove
        node = self.search(value, self.root)
        if node is None or node.value != value:
            return

        # helper to factor out common code from the three cases below
        def promote(to_remove, to_promote):
            if to_remove == self.root:
                self.root = to_promote
            elif to_remove.parent.left == to_remove:
                to_remove.parent.left = to_promote
            else:
                to_remove.parent.right = to_promote

            if to_promote:
                to_promote.parent = to_remove.parent

        if node.left and node.right:
            # in this case we do not have to update node.parent,
            # we update leftmost's parent and then put leftmost.value in node
            leftmost = self.min(node.right)
            promote(leftmost, leftmost.right)
            node.value = leftmost.value
        else:
            promote(node, node.right or node.left)

        self.size -= 1

    def search(self, value, node):
        """
        Returns the node with the given value if found, else returns a potential
        parent node.
        :param value: the value to search for
        :param node: the root of the tree to search within
        :return: the node with value or a valid parent for a node with value
        """
        # if initial search call is made with None node
        if node is None:
            return None

        if node.left and value < node.value:
            return self.search(value, node.left)
        if node.right and value > node.value:
            return self.search(value, node.right)

        return node

    def inorder(self, node):
        """
        Return an iterator to the inorder sequence of nodes.
        :param node: the root of the tree to list
        :return: an iterator to the inorder sequence of nodes in the tree
        """
        if node is None:
            return
        yield from self.inorder(node.left)
        yield node.value
        yield from self.inorder(node.right)

    def preorder(self, node):
        """
        Return an iterator to the preorder sequence of nodes.
        :param node: the root of the tree to list
        :return: an iterator to the preorder sequence of nodes in the tree
        """
        if node is None:
            return
        yield node.value
        yield from self.preorder(node.left)
        yield from self.preorder(node.right)

    def postorder(self, node):
        """
        Return an iterator to the postorder sequence of nodes.
        :param node: the root of the tree to list
        :return: an iterator to the postorder sequence of nodes in the tree
        """
        if node is None:
            return
        yield from self.postorder(node.left)
        yield from self.postorder(node.right)
        yield node.value

    def depth(self, value):
        """
        Return the number of levels separating position p from the root
        Returns the number of ancestors of thee node with value excluding itself
        :param value: the value of the node to find the depth of
        :return depth_of_val: the depth  of the node described above
        """
        node = self.search(value, self.root)

        # if node is not in the tree
        if node is None or node.value != value:
            return -1

        # otherwise ascend to root
        edges = 0
        while node != self.root:
            edges += 1
            node = node.parent
        return edges

    def height(self, node):
        """
        Returns the maximum depth of any node in the tree
        :param node: the root of the tree
        :return: the height of the tree whose root is node
        """
        if node is None:
            return -1
        if not (node.left or node.right): # if node is a leaf
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def min(self, node):
        """
        Return the minimum of the tree rooted at node
        :param node: the root of the tree
        :return: the min value in the tree or None if root is None
        """
        if node is None:
            return None
        # the minimum value will be all the way to the left
        if node.left:
            return self.min(node.left)
        return node

    def max(self, node):
        """
        Return the maximum of the tree rooted at node
        :param node: the root of the tree
        :return: the max value in the tree or None if root is None
        """
        if node is None:
            return None
        # the maximum value will be all the way to the right
        if node.right:
            return self.max(node.right)
        return node

    def get_size(self):
        """
        :return: the number of nodes in the tree
        """
        return self.size

    def is_perfect(self, node):
        """
        Returns whether the given tree is perfect
        :param node: the root of the tree to test
        :return: whether the tree is perfect
        """
        # if the tree has height log(N) and N elements, then the tree is perfect
        nodes_in_perfect_tree = 2 ** (1 + self.height(node)) - 1
        return nodes_in_perfect_tree == self.get_size()

    def is_degenerate(self):
        """
        :return: whether the tree is degenerate
        """
        if self.root is None:
            return False
        height = self.height(self.root.right or self.root.left) + 1
        root_node = 1
        # if all nodes contribute the height
        # then the tree is degenerate
        return height + root_node == self.get_size()
