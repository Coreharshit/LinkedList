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

    def reverse(self):
        prev=None
        Current=self.head
        while(Current is not None):
            next=Current.next
            Current.next=prev
            prev=Current
            Current=next
        self.head=prev

    def printit(self):
        itr=self.head
        while(itr):
            print(itr.data,end="-->")
            itr=itr.next
        print()
if __name__=="__main__":
    ll=LinkedList()
    ll.insert(2)
    ll.insert(5)
    ll.insert(3)
    ll.insert(1)
    ll.printit()
    ll.reverse()
    ll.printit()
