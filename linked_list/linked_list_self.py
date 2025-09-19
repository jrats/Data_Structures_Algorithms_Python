class Node:
    def __init__(self, value):
        self.value = value 
        self.next = None

# new_node = Node(10)
# print(new_node)

class LinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.head = new_node        
    #     self.tail = new_node          #with only one node
    #     self.length = 1
    
    def __init__(self):
        self.head = None
        self.tail = None       #with no node
        self.length = 0


new_linked_list = LinkedList()
print(new_linked_list.head) 
