from Project3.HybridSort import *

l = [1,4,2,4,-1,-5,-3,5]
x = insertion_sort(l,True)
print(x)

y = merge_sort(l, 3, True)
print(y)
l = []
y = merge_sort(l, 3, True)
print(y)
l = [1]
y = merge_sort(l, 3, True)
print(y)



l = [1,1]
y = merge_sort(l, 0, True)
print(y)

l = [1,1]
y = merge_sort(l, 1, True)
print(y)

l = [2,1]
y = merge_sort(l, 1, True)
print(y)

l = []
y = merge_sort(l, 1, True)
print(y)

l = [1,-3]
y = merge_sort(l, 3, True)
print(y)

l = [1, 0,-3]
y = merge_sort(l, 3, True)
print(y)

l = [1, 0,-3]
y = merge_sort(l, 0, True)
print(y)

l = [1, 0,-3]
y = merge_sort(l, 4, True)
print(y)

l = [1, 0,-3]
y = merge_sort(l, 1, True)
print(y)
