import heapq


class Edge:
    def __init__(self, weight, start, target):
        self.start = start
        self.target = target
        self.weight = weight


class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predec = None
        self.neighbors = []
        self.min_distance = float("inf")

    def __lt__(self, other):
        return self.min_distance < other.min_distance

    def add_edge(self, weight, target):
        edge = Edge(weight, self, target)
        self.neighbors.append(edge)


class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, start):
        start.min_distance = 0
        heapq.heappush(self.heap, start)
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbors:
                target = edge.target
                start = edge.start
                weight = edge.weight
                new_dist = weight + start.min_distance
                if new_dist < target.min_distance:
                    target.min_distance = new_dist
                    target.predec = start
                    heapq.heappush(self.heap, target)
            actual_vertex.visited = True

    def get_shortest_path(self, vertex):
        print(f"The shortest distance for {vertex} is {vertex.min_distance}")
        actual_vertex = vertex
        path = []
        while actual_vertex:
            path.append(actual_vertex.name)
            actual_vertex = actual_vertex.predec
        for i in path[:0:-1]:
            print(i, end="->")
        print(path[0], end = "")


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")
G = Node("G")
H = Node("H")

A.add_edge(6, B)
A.add_edge(9, D)
A.add_edge(10, C)
B.add_edge(16, E)
B.add_edge(13, F)
B.add_edge(5,  D)
D.add_edge(8,  F)
D.add_edge(7,  H)
C.add_edge(6,  D)
C.add_edge(5,  H)
C.add_edge(21, G)
E.add_edge(10, G)
F.add_edge(4,  E)
F.add_edge(12, G)
H.add_edge(14, G)
H.add_edge(2, F)

D = Dijkstra()
D.calculate(A)
D.get_shortest_path(E)
