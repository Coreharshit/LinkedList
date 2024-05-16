class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,val):
        if self.head is None:
            self.head=Node(val,None)
            return
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=Node(val,None)
    def remdup(self):
        dummy=self.head
        while(dummy.next ):
            if (dummy.data==dummy.next.data):
                Next=dummy.next.next
                dummy.next=Next
            else:
                dummy=dummy.next
    def printit(self):
        itr=self.head
        while(itr):
            print(itr.data,end="-->")
            itr=itr.next
        print()
if __name__=="__main__":
    ll=LinkedList()
    ll.insert(1)
    ll.insert(1)
    ll.insert(2)
    ll.insert(2)
    ll.insert(2)
    ll.insert(3)
    ll.insert(3)
    ll.insert(3)
    ll.remdup()
    ll.printit()
