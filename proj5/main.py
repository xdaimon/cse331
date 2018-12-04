from Project5.CircularQueue import CircularQueue

cq = CircularQueue(6)
for i in range(5):
    cq.enqueue(i)

for i in range(5):
    cq.dequeue()

for i in range(10):
    cq.enqueue(i)

for i in range(20):
    cq.dequeue()
    cq.enqueue(i + 10)
    print(cq)

