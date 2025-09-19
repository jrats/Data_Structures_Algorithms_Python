class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.items.append(value)
        return "Element inserted at the end of queue"
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None
        return None
    


queue = Queue()
print(queue.isEmpty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(10)
queue.enqueue(100)
queue.dequeue()
print(queue.peek())
print(queue)
print(queue.delete())

    
