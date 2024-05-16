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

    def CheckCircular(self,s):
        dummy=self.head
        while(dummy.next!=self.head ):
            if dummy.next.data==s:
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
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.head.next.next.next.next.next=ll.head
    ll.CheckCircular(3)
    ll.printit()

        

