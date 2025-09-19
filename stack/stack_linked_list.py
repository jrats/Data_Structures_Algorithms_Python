class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.top = new_node
    #     self.length = 1

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if self.top is None:               #can use is_empty method here as well
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def peek(self):
        return self.top 
    
    def is_empty(self):
        return self.length == 0
    
    def clear(self):
        self.top = None
        self.length = 0  
    def peek(self):
        if not self.top:
            return None
        else:
            return self.top.value  


stack = Stack()
stack.push(78)
stack.push(89)
stack.push(67)
print(stack.pop().value)
print(stack.peek().value)
print(stack.is_empty())
stack.clear()
print(stack.top)
