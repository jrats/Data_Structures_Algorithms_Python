class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
class CircularDoublyLinkedList :
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # def __init__(self, value):
    #     new_node = Node(value)
    #     new_node.next = new_node
    #     new_node.prev = new_node
    #     self.head = new_node
    #     self.tail = new_node
    #     self.length = 1

    def __str__(self):
        temp = self.head
        result = ''
        while temp:
            result += str(temp.value)
            temp = temp.next
            if temp == self.head:
                break
            result += '<->'
        return result
            


    def append(self, value):
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            new_node.prev = self.tail
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp == self.head:
                break

    def reverse_traverse(self):
        temp = self.tail
        while temp:
            print(temp.value)
            temp = temp.prev
            if temp ==self.tail:
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
        if index< -self.length or index>self.length -1:
            return None
        if index < 0:
            index = self.length + index
        if index < self.length//2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length -1, index, -1):
                temp = temp.prev
        return temp
    
    def set(self, index, value):
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False
    
    def insert(self, index, value):
        new_node = Node(value)
        if index<0:
            index = self.length + index + 1
        if index<0 or index>self.length :
            return 'Invalid range'
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            prev_node = self.get(index-1)
            new_node.next = prev_node.next
            new_node.prev = prev_node
            prev_node.next.prev = new_node
            prev_node.next = new_node
        self.length += 1

    def pop_first(self):
        if not self.head:
            return None
        popped_node = self.head
        if self.length ==1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if not self.head:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head 
            self.head.prev = self.tail
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        curr = self.get(index)
        if index <0:
            index = self.length + index
        if index<0 or index>self.length-1:
            return None
        elif index == 0:
            curr = self.pop_first()
        elif index == self.length -1:
            curr = self.pop()
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            curr.next = None
            curr.prev = None
        self.length -= 1
        return curr
    
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0

            


cdll = CircularDoublyLinkedList()
print(cdll)
cdll.append(10)
cdll.append(20)
cdll.append(30)
cdll.append(40)
cdll.append(50)
cdll.prepend(60)
print(cdll)
# cdll.prepend(90)
# print(cdll)
# print(cdll.insert(7, 8760))
print(cdll.remove(-6))
print(cdll)
cdll.delete_all()
print(cdll)



        