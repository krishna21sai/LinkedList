class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def Insert(self, data):
        Newnode = Node(data)
        if self.head is None:
            self.head = Newnode
            return
        lnode = self.head
        while lnode.next:
            lnode = lnode.next
        lnode.next = Newnode
    
    def deletenode(self, data):
        dnode = self.head
        dprev = None  # Initialize dprev to None
        while dnode:
            if dnode.data == data:
                if dprev:  
                    dprev.next = dnode.next
                else:  
                    self.head = dnode.next
                return
            dprev = dnode
            dnode = dnode.next 
    
    def print_list(self):
        cnode = self.head
        while cnode:
            print(cnode.data, end=" ")
            cnode = cnode.next 

LinkedList = LinkedList()
LinkedList.Insert(4)
LinkedList.Insert(0)
LinkedList.Insert(2)
LinkedList.Insert(1)
LinkedList.deletenode(4)  
LinkedList.print_list()
