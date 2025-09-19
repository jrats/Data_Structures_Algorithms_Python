import QueueLinkedList as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def __str__(self):
        return self._str_rotated()

    def _str_helper(self, level=0, relation="Root", parent = None):
        if parent is None:
            ret = "    "* level + f"{relation}:{self.data}\n"
        else:
            ret = "    "* level + f"{relation} of {parent}: {self.data}\n"
        
        if self.leftChild:
            ret += self.leftChild._str_helper(level+4, "Left", self.data)
        if self.rightChild:
            ret += self.rightChild._str_helper(level+4, "Right", self.data)
        return ret
    
    def _str_rotated(self, level=0):
        ret = ""
        if self.rightChild:
            ret += self.rightChild._str_rotated(level +2)

        ret += "    " * level + str(self.data) + "\n"

        if self.leftChild:
            ret += self.leftChild._str_rotated(level+2)
        return ret

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <=rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)

    return "The node has been successfully inserted"

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        custQueue = queue.Queue()
        custQueue.enqueue(rootNode)
        while not(custQueue.isEmpty()):
            root = custQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                custQueue.enqueue(root.value.leftChild )
            if root.value.rightChild is not None:
                custQueue.enqueue(root.value.rightChild )

def search(rootNode, nodeValue):
    if rootNode is None:
        return "Sorry! The value is not found"
    if rootNode.data == nodeValue:
        return "The value is found"
    elif nodeValue < rootNode.data:
        return search(rootNode.leftChild, nodeValue)
    else:
        return search(rootNode.rightChild, nodeValue) 

   
def minValNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp 
        temp = minValNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

def deleteBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been deleted"


        




bst = BSTNode(None)
print(insertNode(bst, 70))
print(insertNode(bst, 60))
print(insertNode(bst, 50))
print(insertNode(bst, 100))
print(insertNode(bst, 65))
print(insertNode(bst, 80))
print(insertNode(bst, 90))
print(insertNode(bst, 110))
print(bst)
print(deleteNode(bst, 100))
print(bst)
print(deleteBST(bst))
print(bst)
