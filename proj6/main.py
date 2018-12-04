from Project6.BinarySearchTree import BinarySearchTree

# bt = BinarySearchTree()
# bt.insert(1)
# bt.insert(2.5)
# print(bt.search(2.5, bt.root))
# print(bt.depth(2.5))
# print(bt.max(bt.root))
# bt.remove(2.5)
# bt.remove(1)
# print(bt.max(bt.root))
# for i in range(16):
#     x = (3 - i) % 4 + 4*(i // 4)
#     print(bt.insert(x))
#     print(bt.search(x, bt.root))
# for i in range(16):
#     bt.remove(i)
#     print('remove',i,' but still in tree?:', bt.search(i, bt.root))
#
# for i in range(16):
#     x = (3 - i) % 4 + 4*(i // 4)
#     print(bt.insert(x))
#     print(bt.search(x, bt.root))
#
# for i in bt.preorder(bt.root):
#     x = i.left is None and i.right is None
#     if x:
#         print(i,end = ', ')
# print()
# for i in bt.inorder(bt.root):
#     x = i.left is None and i.right is None
#     if x:
#         print(i,end = ', ')
# print()
# for i in bt.postorder(bt.root):
#     x = i.left is None and i.right is None
#     if x:
#         print(i,end = ', ')
# print()
#
# bt2 = BinarySearchTree()
# bt2.insert(4)
# bt2.insert(5)
# bt2.insert(3)
# print(bt2.is_degenerate())
#
# print(bt2.is_perfect(bt2.root))



bst = BinarySearchTree()
bst.insert(14)
bst.insert(7)
bst.insert(21)
bst.insert(3)
bst.insert(10)
bst.insert(17)
bst.insert(25)
print(bst.is_perfect(bst.root))
