import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

bt = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
bt.leftChild = leftChild
bt.rightChild = rightChild
leftChild.leftChild = tea
leftChild.rightChild = coffee


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
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def search(rootNode, nodeValue):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data==nodeValue:
                return "Successfully found"
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
        return "Not Found!"
    
def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        custQueue = queue.Queue()
        custQueue.enqueue(rootNode)
        while not (custQueue.isEmpty()):
            root = custQueue.dequeue()
            if root.value.leftChild is not None:
                custQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Succesful insertion"
            if root.value.rightChild is not None:
                custQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Succesful insertion"
            
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        custQueue = queue.Queue()
        custQueue.enqueue(rootNode)
        while not(custQueue.isEmpty()):
            root = custQueue.dequeue()
            if root.value.leftChild is not None:
                custQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                custQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode
    
def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        custQueue = queue.Queue()
        custQueue.enqueue(rootNode)
        while not(custQueue.isEmpty()):
            root = custQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    custQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    custQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode, node):

    if not rootNode:
        return "The BT does not exist"
    else:
        custQueue = queue.Queue()
        custQueue.enqueue(rootNode)
        while not(custQueue.isEmpty()):
            root = custQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if root.value.leftChild is not None:
                custQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                custQueue.enqueue(root.value.rightChild)
        return "Failed to delete"
    
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "BT successfully deleted"


deleteBT(bt)
levelOrderTraversal(bt)
    



    






            

    


