from Project7.HashTable import *

ht = HashTable()
for i in range(32):
    ht.insert(str(i), str(i))
    print(ht.size, ht.capacity)
ht.delete('hi')
print(ht.lookup("hi"))
print(ht.lookup("bye"))
print(ht.lookup('1'))
print(ht.lookup('2'))
print(ht.lookup('3'))
print(ht.lookup('4'))
print(ht.lookup('5'))

print(string_difference('hi', 'byi'))
print(string_difference('red', 'blue') == {'r', 'd', 'u','l', 'b'})
print(string_difference('mississippi', 'misipe') == {'ii', 'sss', 'p', 'e'})
print(string_difference('a', 'b'))
