'''Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.'''

import collections
import random

Node = collections.namedtuple("Node", ['value', 'edges'])


def generator(n):
    gen_l = []
    for i in range(n):
        l = Node(i, [])
        gen_l.append(l)
    for i in range(n):
        d = gen_l[i]
        for j in range(i + 1, n):
            if random.random() < 0.5:
                d.edges.append(gen_l[j])
    return gen_l[0]


def dfs(node: Node, value):
    if node.value == value:
        return True
    for edge in node.edges:
        if dfs(edge, value):
            return True
    return False


my_graf = generator(7)
print(my_graf)
print(dfs(my_graf, 5))
