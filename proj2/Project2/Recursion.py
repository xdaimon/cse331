"""
PROJECT 2 - Recursion
Name: Bradley Bauer
"""

from Project2.LinkedNode import LinkedNode


def insert(value, node=None):
    """
    Insert a node into the list
    :param value: value of the node to insert
    :param node: pointer to the next node of the node to insert
    """
    if node is None:
        return LinkedNode(value, None)
    if value <= node.value:
        return LinkedNode(value, node)
    else:
        node.next_node = insert(value, node.next_node)
    return node


def string(node):
    """
    Represent the linked list as a string
    :param node: the head of the linked list
    """
    if node is None:
        return ''
    if node.next_node is None:
        return str(node.value)
    else:
        return str(node.value) + ', ' + string(node.next_node)


def reversed_string(node):
    """
    Represent the reverse of the linked list as a string
    :param node: the head of the linked list
    """
    if node is None:
        return ''
    # if at tail
    if node.next_node is None:
        return str(node.value)
    else:
        return reversed_string(node.next_node) + ', ' + str(node.value)


def remove(value, node):
    """
    Remove the first node with the given value
    :param value: the value of the node to remove
    :param node: the head of the linked list
    """
    # if the head of the linked list has value, then remove the head
    # end the recursion.
    # otherwise recurse on the sublist with head = node.next_node
    if node is None:
        return None
    if node.value == value:
        temp = node.next_node
        del node
        node = temp
    else:
        node.next_node = remove(value, node.next_node)
    return node


def remove_all(value, node):
    """
    Remove all the nodes with the given value
    :param value: the value of the node to remove
    :param node: the head of the linked list
    """
    # while the head of the linked list has value, remove the head.
    # otherwise recurse on the sublist with head = node.next_node
    if node is None:
        return None
    if node.value == value:
        temp = node.next_node
        del node
        node = remove_all(value, temp)
    else:
        node.next_node = remove_all(value, node.next_node)
    return node


def search(value, node):
    """
    Check whether the linked list contains a node with value.
    :param value: the value of the node to search for
    :param node: the head of the linked list
    """
    if node is None:
        return False
    return value == node.value or search(value, node.next_node)


def length(node):
    """
    Return the length of the linked list
    :param node: the head of the linked list
    """
    if node is None:
        return 0
    return 1 + length(node.next_node)


def sum_all(node):
    """
    Sum the values of all nodes in the linked list
    :param node: the head of the linked list
    """
    if node is None:
        return 0
    return node.value + sum_all(node.next_node)


def count(value, node):
    """
    Count the number of nodes that have node.value = value.
    :param value: the value a node must have in order to be counted
    :param node: the head of the linked list
    """
    if node is None:
        return 0
    return int(node.value == value) + count(value, node.next_node)
