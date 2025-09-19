class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        
        self.length += 1

    def __str__(self):
        temp = self.head
        result = ''
        while temp:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += '->'
        return result
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length+=1

    def insert(self, index, value):
        new_node = Node(value)
        if index < - self.length or index >self.length:
            raise Exception("Index out of bounds")
        if index<0:
            index = self.length+index
        if index == 0:
            if self.length==0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = self.head
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(index -1):
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node
        self.length+=1

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp== self.head:
                break

    def search(self, target):
        temp = self.head
        while temp:
            if temp.value == target:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False
    
    def get(self, index):
        if index< -self.length or index>=self.length:
            return None
        if index <0:
            index = self.length +index
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set(self, index, value):
        temp = self.get(index)
        while temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        popped_node = self.head
        if self.length ==0:
            return None
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        popped_node = self.tail
        if self.length ==0:
            return None
        if self.length ==1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next 
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        if index< -self.length or index>=self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            prev_node = self.get(index-1)
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        if self.length ==0:
            return None
        self.tail.next = None
        self.head = None
        self.tail = None

    def delete_by_val(self, value):
        if self.length ==0:
            return False
        if self.head == self.tail and self.tail.value == value:
            self.head = None
            self.tail = None
            self.length = 0
            return True
        
        prev = None
        current = self.head
        while True:
            if current.value == value:
                if current == self.head:
                    self.head = current.next
                    self.tail.next = self.head
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev 
                self.length -= 1
                return True
            
            prev = current
            current = current.next
            if current == self.head:
                break 
        return False
        




            


cs = CSLinkedList()
cs.append(12)
cs.append(14)
cs.append(16)
cs.append(16)
cs.append(80)
cs.prepend(100)
cs.prepend(110)
# cs.insert(7, 750)
# print(cs.tail.next.value)
# print(cs.head.next.value)
# print(cs)
# cs.traverse()
# print(cs.search(16))
# print(cs.get(-10))
# print(cs.set(-2, 1000))
# print(cs)
# print(cs.pop_first()) 
print(cs)
print(cs.delete_by_val(14))
print(cs)

    




