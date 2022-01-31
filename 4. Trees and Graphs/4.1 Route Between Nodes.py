# base definition
from collections import deque


# Solution. BFS
class State:
    Unvisited = 0
    Visiting = 1
    Visited = 2


class Node:
    def __init__(self, v):
        self.data = v
        self.adjacent = []
        self.state = State.Unvisited

    def __repr__(self):
        return f"Node({self.data})"

    def get_adjacent(self):
        return self.adjacent


class Graph:
    def __init__(self, graph):
        self.data = graph

    def __repr__(self):
        return "Graph"

    def get_nodes(self):
        return [key for key in self.data]


def search(g, start, end):
    if start == end:
        return True

    # operates as Queue
    q = deque([])

    for u in g.get_nodes():
        u.state = State.Unvisited
    start.state = State.Visiting
    q.append(start)
    while q:
        u = q.popleft()  # dequeue()
        if u is not None:
            for v in u.get_adjacent():
                if v.state == State.Unvisited:
                    if v == end:
                        return True
                    else:
                        v.state = State.Visiting
                        q.append(v)
            u.state = State.Visited
    return False


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node0.adjacent = [node1, node3]
node1.adjacent = [node2]
node3.adjacent = [node5]
node4.adjacent = [node5]
node5.adjacent = [node1, node2]
g = Graph([node0, node1, node2, node3, node4, node5])
print(search(g, node0, node5))


# My Solution.
def bfs(graph, start, end):
    visited = [False for _ in range(len(graph.keys()))]
    q = deque([start])

    while q:
        v = q.popleft()
        if visited[v]:
            continue
        visited[v] = True
        if visited[end]:
            break
        for adj in graph[v]:
            if not visited[adj]:
                q.append(adj)
    return visited[end]


# g = {0: [2], 1: [], 2: [3], 3: [0]}
# print(bfs(g, 0, 2))
