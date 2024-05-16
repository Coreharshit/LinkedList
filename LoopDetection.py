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

    def loop(self):
        slow=self.head
        fast=self.head
        slow=slow.next
        fast=fast.next.next
        while(fast and fast.next):
            if (slow==fast):
                break
            slow=slow.next
            fast=fast.next.next
        
        if (slow != fast):
            return False
        else:
            return True

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
    ll.insert(2)
    ll.head.next.next.next.next=ll.head.next
    print(ll.loop())

        


