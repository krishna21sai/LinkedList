class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def Insert(self,data):
        Newnode = Node(data)
        if self.head is None:
            self.head = Newnode
            return
        lnode = self.head
        while lnode.next:
            lnode = lnode.next
        lnode.next = Newnode
    def print_list(self):
        cnode = self.head
        while cnode:
            print(cnode.data,end = " ")
            cnode = cnode.next 

Linkedlist  = LinkedList()
Linkedlist.Insert(4)
Linkedlist.Insert(0)
Linkedlist.Insert(2)
Linkedlist.Insert(1)
Linkedlist.print_list()
