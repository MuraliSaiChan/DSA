class Graph:
    def __init__(self):
        self.adjacentList = {}

    def get_sample(self):
        self.adjacentList = {'A': ['B', 'C', 'D'],
                                'B' : ['A', 'C'],
                                'C' : ['A', 'B'],
                                'D' : ['A']
                             }
        return self.adjacentList

    def add_vertex(self,vertex):
        if vertex not in self.adjacentList.keys():
            self.adjacentList[vertex] = []
            return True
        return False

    def remove_vertex(self, v):
        if v in self.adjacentList.keys():
            for i in self.adjacentList[v]:
                self.adjacentList[i].remove(v)
            self.adjacentList.pop(v)
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adjacentList.keys() and v2 in self.adjacentList:
            self.adjacentList[v1].append(v2)
            self.adjacentList[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        l = self.adjacentList.keys()
        if v1 in l and v2 in l:
            try:
                self.adjacentList[v1].remove(v2)
                self.adjacentList[v2].remove(v1)
            except ValueError as v:
                print("No edge between two vertices {} and {}."\
                      .format(v1,v2))
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacentList:
            print(vertex,":",self.adjacentList[vertex])

    def bfs(self, vertex):
        queue = [vertex]
        visited = [vertex]
        while queue != []:
            temp = queue.pop(0)
            for i in self.adjacentList[temp]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        print(visited)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack != []:
            temp = stack.pop()
            print(temp)
            for i in self.adjacentList[temp]:
                if i not in visited:
                    stack.append(i)
                    visited.append(i)
        print(visited)



graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_edge("A","C")
graph.add_edge("A","E")
graph.add_edge("A","D")
graph.add_edge("B","C")
graph.add_edge("B","E")
graph.add_edge("B","D")
graph.add_edge("C","D")
graph.add_edge("E","D")
# graph.remove_edge("A","C")
# graph.remove_edge("A","D")
# print("\nBefore Deleting\t:")
# graph.print_graph()
# #graph.remove_vertex("A")
# print("\nAfter Deleting\t:")
graph.print_graph()
print("BFS")
graph.bfs("A")
print("DFS")
graph.dfs("A")