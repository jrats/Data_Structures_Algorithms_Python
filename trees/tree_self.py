class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        self.children = children if children is not None else []

    def __str__(self,level=0):
        ret = "   " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level +1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)



cola = TreeNode('Cola', [])
soda = TreeNode('Soda', [])
coffee = TreeNode('Coffee', [])
tea = TreeNode('Tea', [])
cold = TreeNode('Cold',[cola, soda])
hot = TreeNode('Hot', [coffee, tea])
tree = TreeNode('Drinks',[cold , hot])
# tree.addChild(cold)
# tree.addChild(hot)
# cold.addChild(cola)
# cold.addChild(soda)
# hot.addChild(coffee)
# hot.addChild(tea)
print(tree)
