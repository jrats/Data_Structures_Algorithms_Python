# parent[v] → stores the representative (root) of the set containing v.

# rank[v] → stores the "approximate height" of the tree rooted at v. Used for balancing.

# find(x) → follows parent pointers until reaching the root (a node that is its own parent).

# union(x, y) → merges the sets of x and y, making one root the parent of the other. Chooses root based on rank to keep tree shallow.


class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):                         #can apply path compression here as well for all elements to directly point to the root for O(1) time lookups in the following calls
        if self.parent[item] == item:             #recurse till we find the root, where the parent of the item and the item are the same
            return item
        else:
            return self.find(self.parent[item])
        
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1                #Both trees have the same height. When we attach one under the other, the resulting tree’s height increases by 1.That’s why we increment rank[xroot] (or whichever becomes the new root).



vertices = ['A', 'B', 'C', 'D', 'E']
ds = DisjointSet(vertices)
ds.union('A', 'E')
ds.union('B', 'E')
print(ds.find('B'))