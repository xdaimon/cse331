from Project6.BinarySearchTree import BinarySearchTree as stu

bst = stu()

bst.insert(21)
bst.insert(10)
bst.insert(32)
bst.insert(5)
bst.insert(16)
bst.insert(27)
bst.insert(39)

assert bst.depth(5) == 2
assert bst.depth(10) == 1

assert bst.height(bst.root) == 2
assert bst.height(bst.root.left) == 1
