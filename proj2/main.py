import Project2.Recursion as r
from Project2.LinkedNode import LinkedNode

linked_node = r.insert(1)
linked_node = r.insert(2, linked_node)
linked_node = r.insert(4, linked_node)
linked_node = r.insert(3, linked_node)
linked_node = r.insert(2, linked_node)

print("ORIGINAL:", r.string(linked_node))
linked_node = r.remove_all(2, linked_node)

print("REMOVE 2:", r.string(linked_node))
print("EXPECTED: 1, 3, 4")

for num in range(1,5):
	if num != 2:
		assert type(linked_node) == LinkedNode
		assert linked_node.value == num
		linked_node = linked_node.next_node
	
