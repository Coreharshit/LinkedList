# 1->2->3->4->5
# 5->1->2->3->4

class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,value):
        if(self.head is None):
            self.head=Node(value,None)
            return
        itr=self.head
        while(itr.next):
            itr=itr.next
        itr.next=Node(value,None)
    def printf(self):  
        if self.head is None:
            return
        l=self.head
        while(l):
            print(l.data,end="->")
            l=l.next
        print()
    def reep(self):
        p=self.head
        while(p.next.next):
            p=p.next
        crr=p.next
        p.next=p.next.next
        crr.next=self.head
        self.head=crr

if __name__=="__main__":
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.printf()
    ll.reep()
    ll.printf()
