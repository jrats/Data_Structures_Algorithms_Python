import QueueLinkedList as queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1+ max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1+ max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1+ max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1+ max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    rootNode.height = 1+ max(getHeight(rootNode.rightChild), getHeight(rootNode.leftChild))
    balance = getBalance(rootNode)
    if balance >1 and nodeValue<rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue>rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance< -1 and nodeValue>rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance<-1 and nodeValue<rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def deleteNode(rootNode, nodeValue):
    if not rootNode:
        return rootNode
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    rootNode.height = 1+max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >=0:
        return rightRotate(rootNode)
    if balance < 1 and getBalance(rootNode.rightChild) <=0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) <0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < 1 and getBalance(rootNode.rightChild) >1:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL tree has been successfully deleted"



avl = AVLNode(30)
avl = insertNode(avl, 25)
avl = insertNode(avl, 35)
avl = insertNode(avl, 20)
avl = insertNode(avl, 15)
avl = insertNode(avl, 5)
avl = insertNode(avl, 10)
avl = insertNode(avl, 50)
avl = insertNode(avl, 60)
avl = insertNode(avl, 70)
avl = insertNode(avl, 65)
avl = deleteNode(avl, 60)
levelOrderTraversal(avl)
print(avl)
deleteAVL(avl)
print(avl)