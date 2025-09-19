from collections import defaultdict          # defaultdict is a special kind of dictionary from the collections module

class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberofVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack):
        visited.add(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        
        stack.append(v)

    def topologicalSort(self):
        visited = set()
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)

        print(stack[::-1])


g= Graph(8)
g.addEdge('A', 'C')
g.addEdge('C', 'E')
g.addEdge('E', 'H')
g.addEdge('E', 'F')
g.addEdge('F', 'G')
g.addEdge('B', 'D')
g.addEdge('B', 'C')
g.addEdge('D', 'F')

g.topologicalSort()