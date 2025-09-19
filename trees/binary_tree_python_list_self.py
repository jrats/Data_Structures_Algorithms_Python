class BinaryTree:
    def __init__(self, size):
        self.custList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size 

    def insertNode(self,value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.custList[self.lastUsedIndex +1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"
    
    def searchNode(self, nodeValue):
        for i in range(len(self.custList)):
            if self.custList[i] == nodeValue:
                return 'Success'
        return "Not found"
    
    def preOrderTraversal(self, index):
        if index>self.lastUsedIndex:
            return
        print(self.custList[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)

    def inOrderTraversal(self, index):
        if index>self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.custList[index])
        self.inOrderTraversal(index*2 + 1)

    def postOrderTraversal(self, index):
        if index>self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 + 1)
        print(self.custList[index])

    def levelOrderTraversal(self, index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.custList[i])

    def deleteNode(self, value):
        if self.lastUsedIndex ==0:
            return "No node to delete"
        for i in range(1, self.lastUsedIndex+1):
            if self.custList[i] == value:
                self.custList[i] = self.custList[self.lastUsedIndex]
                self.custList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been deleted"
        return "Node to delete not found"
    
    def deleteBT(self):
        self.custList = None
        return "The BT has been deleted"



bt = BinaryTree(8)
print(bt.insertNode("Drinks"))
print(bt.insertNode("Hot"))
print(bt.insertNode("Cold"))
print(bt.insertNode("Tea"))
print(bt.insertNode("Coffee"))
print(bt.searchNode('Cola'))
print(bt.deleteBT())
bt.levelOrderTraversal(1)

