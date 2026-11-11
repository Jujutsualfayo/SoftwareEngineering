class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        current = self.head

        while current is not None:
              print(current.value)
              current = current.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
         current = current.next
        
        current.next = new_node
        
    def prepend(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node  
    def delete(self, value):
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            return True
        current = self.head
        while current.next is not None:
            if current.next.value == value:
             current.next = current.next.next
            return True
        current = current.next
                
        return False
        
    
my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.print_list()
    
        
    
        
        
        



