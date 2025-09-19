class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    # def __str__(self):
    #     return f"{self.prev} <- {self.value} -> {self.next}"
    
    def __str__(self):
        return str(self.value)


# new_node = Node(10)
# print(new_node)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp = self.head
        result = ''
        while temp:
            result += str(temp.value)
            if temp.next is not None:
                result += '<->'
            temp = temp.next
        return result
            
        
    def append(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next 

    def reverse_traverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev 

    def search(self, target):
        temp = self.head
        index = 0
        while temp:
            if temp.value == target:
                return index
            temp = temp.next
            index += 1
        return -1
    
    def get(self, index):
        if index < -self.length or index> self.length - 1:
            return None
        if index < 0:
            index = self.length + index
        if index< self.length //2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail 
            for _ in range(self.length -1, index, -1):
                current_node = current_node.prev
        return current_node
    
    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index <0:
            index = self.length + index +1
        if index<0 or index>self.length :
            return None
        elif index ==0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            new_node = Node(value)
            temp_node = self.get(index -1)
            new_node.next = temp_node.next
            new_node.prev = temp_node
            temp_node.next.prev = new_node
            temp_node.next = new_node
        self.length += 1

    def pop_first(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = popped_node.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            self.tail = self.tail.prev 
            self.tail.next = None
            popped_node.prev = None
        self.length -=1
        return popped_node
    
    def remove(self, index):
        if index <0:
            index = self.length + index 
        if index<0 or index>self.length :
            return None
        elif index ==0:
            popped_node=self.pop_first()
        elif index == self.length-1:
            popped_node=self.pop()
        else:
            popped_node = self.get(index)
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.next = popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        self.head = self.tail = None
        self.length = 0






dll = DoublyLinkedList()
dll.append(12)
dll.append(22)
dll.prepend(45)
dll.prepend(60)
# dll.traverse()
# dll.reverse_traverse()
# print(dll.search(22))
# print(dll.get(5))
# print(dll)
# print(dll.set(-5,1900))
print(dll)
# dll.insert(-3, 500)
# print(dll)
# print(dll.tail)
# print(dll)
# print(dll.remove(-1))
dll.delete_all()
print(dll)


