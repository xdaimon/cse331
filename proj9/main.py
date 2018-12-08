from Project9.Graph import *

# g = Graph(filename='email.txt')
# g = Graph(filename='test')
g = Graph(size = 20, connectedness=.1)
# g = Graph(size = 996, connectedness=1)

# print(g.BFS(3,50))
# print(g.DFS(1,5))
for i,vo in sorted(g.adj_list.items()):
    # print(vo, '::', vo.edges)
    en = []
    for e in vo.edges:
        en.append((e.source.ID,e.destination))
    print(vo, en)
print(fake_emails(g, True))
for i,vo in sorted(g.adj_list.items()):
    # print(vo, '::', vo.edges)
    en = []
    for e in vo.edges:
        en.append((e.source.ID,e.destination))
    print(vo, en, end=' ')
    print(vo.visited, end=' ')
    print(vo.fake)

print(g==g)

# for i in range(1000):
#     st = g.BFS(i, 111)
#     if str(st) == 'Path: \n':
#         continue
#     print(st)

# print(g.DFS(2, 4))
# for i in range(1000):
#     st = g.DFS(i, 574)
#     if str(st) == 'Path: \n':
#         continue
#     print(st)

# print(fake_emails(g))
