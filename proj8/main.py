from Project8.BinaryMinHeap import BinaryMinHeap as Heap
from Project8.BinaryMinHeap import heap_sort
from random import randint
import heapq

h = Heap()

h.pop_min()

for i in range(16):
    h.heap_push(randint(0, 99))

print(h)
h.heap_pop(h.table[4])
print(h)
h.heap_pop(h.table[-1])
print(h)
h.heap_pop(h.table[0])
print(h)

# for i in range(h.get_size()):
#     h.heap_pop(h.table[0])
# print(h)

sort = [None]*h.get_size()
for j in range(len(sort)):
    sort[j] = h.pop_min()

print(sorted(sort) == sort)

for j in range(1000):
    l = []
    for i in range(16):
        l.append(randint(0,100))
    hs = heap_sort(l.copy())
    if sorted(list(set(l))) != hs:
        print(sorted(list(set(l))), hs)


# use repated pop_min() on the heap to sort in O(nlogn)
# there are atleast as many O(log(n)-1) percolate_down calls as there are
# leafs in the tree which is ceil(n/2). So the work contributed by the leafs
# is work_leafs=ceil(n/2)(log(n)-1)) but since half the nodes in the tree
# are leafs the total amount of work done is \leq 2 * work_leafs.
# so this usage of heapsort costs O(nlogn)
