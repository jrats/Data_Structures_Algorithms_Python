from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,':',self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            for key in self.adjacency_list[vertex]:
                self.adjacency_list[key].remove(vertex)
            del self.adjacency_list[vertex]
            return True
        return False
    
    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            cur_vertex = queue.popleft()
            print(cur_vertex)
            for adj_vertex in self.adjacency_list[cur_vertex]:
                if adj_vertex not in visited:
                    visited.add(adj_vertex)
                    queue.append(adj_vertex)

    def dfs(self, vertex):
        visited = set()
        stack=[vertex]
        while stack:
            cur = stack.pop()
            if cur not in visited:
                print(cur)
                visited.add(cur)
            for adj_vertex in self.adjacency_list[cur]:
                if adj_vertex not in visited:
                    stack.append(adj_vertex)

    def dfs_recursive(self, vertex, visited=None):
        if not visited:
            visited = set()
        visited.add(vertex)
        print(vertex)

        for adj_vertex in self.adjacency_list[vertex]:
            if adj_vertex not in visited:
                self.dfs_recursive(adj_vertex, visited)
            




g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')
g.add_vertex('E')
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('E', 'B')
g.add_edge('E', 'D')
g.add_edge('D', 'C')
# g.print_graph()
# g.remove_vertex('A')
# g.print_graph()
g.dfs_recursive('A')
