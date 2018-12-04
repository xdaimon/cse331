import LinkedList as ll

#x = ll.LinkedList()
#for i in range(1, 20):
#    x.push_back(i)
#for i in range(1, 20):
#    print(x.pop_front())
#
#for i in range(1, 19):
#    x.push_back(i)
#x.reverse_list()
#for i in range(1, 19):
#    print(x.pop_front())
#
#print(x.size)

#x = ll.LinkedList()
#for i in range(1, 20):
#    x.push_back(i)
#for i in range(1, 20):
#    print(x.pop_back())
#print(x.size)
#print(x.head)
#print(x.tail)
#x.reverse_list()
#print(x.size)
#print(x.head)
#print(x.tail)
#x.push_back(5)
#x.push_back(6)
#x.reverse_list()
#print(x.size)
#print(x.head)
#print(x.tail)


x = ll.LinkedList()
for i in range(0, 2):
    x.push_back(i)
x.reverse_list()
print('front: ', x.front_value())
print('back: ', x.back_value())
