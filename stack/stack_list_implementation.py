class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        values = [ str(x) for x in reversed(self.items)]
        return '\n'.join(values)
    
    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def clear(self):
        self.items = []


my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
print(my_stack.peek())
print(my_stack)
print(my_stack.size())
my_stack.clear()
print(my_stack)
print(len(my_stack.items))