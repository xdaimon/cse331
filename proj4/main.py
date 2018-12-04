from Project4.Stack import *

stack = Stack()
for i in range(0, 18):
        stack.push(i%4)

stack = replace(stack, 3, 8)

print("Output: ", str(stack))

