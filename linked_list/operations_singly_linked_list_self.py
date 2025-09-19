#insertion to a singly linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else :
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1

    def insert(self, value, index):
        new_node = Node(value)
        if index>self.length or index<-self.length:
            return False
        if index<0:
            index = self.length + index + 1
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length +=1
        return True



    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result
    
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index +=1
        return -1
    
    def get(self, index):
        if index<-self.length or index> self.length:
            return False
        if index<0:
            index = self.length + index 
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        if self.length == 0:
            return None
        current = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = current.next
            current.next = None
        self.length -=1
        return current
    
    def pop(self):
        if self.length == 0:
            return None
        pop_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        self.length -= 1
        return pop_node
    
    def remove(self, index):
        if index<-self.length or index>self.length or self.length==0:
            return None
        if index < 0:
            index = self.length + index
        if index ==0:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next = None
            if self.length == 1:
                self.tail = None
        else:
            temp = self.get(index -1)
            popped_node = temp.next 
            temp.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    

ll = LinkedList()
ll.prepend(0)
ll.append(10)
ll.append(20)
ll.append(30)
ll.prepend(5)
ll.prepend(2)
ll.insert(50, 3)
ll.traverse()
print(ll.get(-1))
# print(ll.set(2, 100))
print(ll)
# print(ll.remove())
print(ll.delete())
print(ll)      #printed using __str__ method




            



