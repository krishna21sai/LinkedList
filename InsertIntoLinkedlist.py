class Node:
    def __init__(self,data):
        self.data = data
        self.next = None



class Linkedlist:
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
        
    def InsertatPosition(self,pos,data):
        inode = self.head


        i = 1
        nnode = Node(data)

        while i<pos and inode.next!=None:
            inode = inode.next
            knode = inode.next
            i+=1


        if(i<pos):
            print("position is greater than size of linked list")
            return
        
        inode.next = nnode
        inode.next.next = knode


llist = Linkedlist()


llist.Insert(3)
llist.Insert(4)
llist.Insert(5)
llist.Insert(8)


llist.InsertatPosition(3,9)


llist.print_list()


