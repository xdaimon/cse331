from Project6.BinarySearchTree import BinarySearchTree as stu

bst = stu()

bst.insert(14)
bst.insert(7)
bst.insert(21)
bst.insert(3)
bst.insert(10)
bst.insert(17)
bst.insert(25)

gen1 = bst.preorder(bst.root)
gen2 = bst.postorder(bst.root)
gen3 = bst.inorder(bst.root)

pre = [14,7,3,10,21,17,25]
post = [3,10,7,17,25,21,14]
inorder = [3,7,10,14,17,21,25]

for i in range(7):
    x1 = next(gen1, None)
    x2 = next(gen2, None)
    x3 = next(gen3, None)
    print(x1, pre[i])
    print(x2, post[i])
    print(x3, inorder[i])
    assert x1 == pre[i]
    assert x2 == post[i]
    assert x3 == inorder[i]


