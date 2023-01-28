from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v ,e):
        self.graph[v].append(e)

    def topo_util(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topo_util(i,visited,stack)
        stack.insert(0, v)

    def toposort(self):
        visited = []
        stack   = []
        for i in list(self.graph):
            if i not in visited:
                self.topo_util(i, visited, stack)
        print(stack)

graph = Graph()
graph.add_edge("A","C")
graph.add_edge("A","D")
graph.add_edge("A","E")
graph.add_edge("C","B")
graph.add_edge("E","B")
graph.add_edge("D","B")
graph.add_edge("D","E")
graph.add_edge("C","D")

graph.toposort()

