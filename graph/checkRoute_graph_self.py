from collections import deque

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    #DFS
    # def checkRoute(self, startNode, endNode, visited=None):
    #     if visited is None:
    #         visited = set()
    #     if startNode == endNode:
    #         return True
    #     visited.add(startNode)
    #     for node in self.gdict.get(startNode,[]):
    #         if node not in visited:
    #             if self.checkRoute(node, endNode, visited):
    #                 return True
    #     return False

    #BFS
    def checkRoute(self, startNode, endNode):
        visited = set()
        queue = deque([startNode])
        
        while queue:
            node = queue.popleft()
            if node == endNode:
                return True
            if node not in visited:
                visited.add(node)
                queue.extend(self.gdict.get(node, []))
                
        return False
    