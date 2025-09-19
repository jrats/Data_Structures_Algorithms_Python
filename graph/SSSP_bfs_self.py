class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def SSSP_bfs(self, start, end):
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adj in self.gdict.get(node, []):
                new_path = list(path)
                new_path.append(adj)
                queue.append(new_path)

cust_dict = { "a": ["b", "c"],
              "b": ["d", "g"],
              "c": ["d", "e"],
              "d": ["f"], 
              "e": ["f"],
              "g": ["f"]}
g = Graph(cust_dict)
print(g.SSSP_bfs('a','e1'))