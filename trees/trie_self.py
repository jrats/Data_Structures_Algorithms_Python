class TrieNode:
    def __init__(self):
        self.children = {}     #dictionary to create links between nodes and their children
        self.endOfString = False      #since we are creating a blank node to begin with

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i 
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True 
        print('Inserted successfully')

    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if not node:
                return False
            currentNode = node

        if currentNode.endOfString == True:
            return True
        else:
            return False
        
def deleteString(root, word, index):
    # ch = word[index]
    # currentNode = root.children.get(ch)
    # canThisNodeBeDeleted = False

    # if len(currentNode.children)>1:
    #     deleteString(currentNode, word, index+1)
    
    # if index == len(word) - 1:
    #     if len(currentNode.children) >= 1:
    #         currentNode.endOfString = False
    #         return False
    #     else:
    #         root.children.pop(ch)
    #         return True
    # if currentNode.endOfString == True:
    #     deleteString(currentNode, word, index +1)
    #     return False
    
    # canThisNodeBeDeleted = deleteString(currentNode, word, index +1)
    # if canThisNodeBeDeleted == True:
    #     root.children.pop(ch)
    #     return True
    # else:
    #     return False

    if index == len(word):
        if not root.endOfString:
            return False
        root.endOfString = False
        return len(root.children) == 0
    
    ch = word[index]
    currentNode = root.children.get(ch)
    if not currentNode:
        return False 
    
    shouldDeleteChild = deleteString(currentNode, word, index+1)

    if shouldDeleteChild:
        root.children.pop(ch)
        return len(root.children)==0 and not root.endOfString
    
    return False
    
    
    

    
    
    


    


trie = Trie()
trie.insertString('App')
trie.insertString('Apple')
deleteString(trie.root, 'App', 0)
print(trie.searchString("App"))


