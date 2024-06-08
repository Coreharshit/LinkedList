'''
Input:
N = 2
LinkedList: 1->2->3->4->5->6->7->8->9
Output: 8
Explanation: In the first example, there
are 9 nodes in linked list and we need
to find 2nd node from end. 2nd node
from end is 8.
'''

class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class Linked:
    def __init__(self):
        self.head=None
    def insert(self,value):
        if self.head is None:
            self.head=Node(value,None)
        else:
            p=self.head
            while p.next:
                p=p.next
            p.next=Node(value,None)
    def rev(self):
        prev=None
        current=self.head
        while(current is not None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=prev
    def printl(self):
        x=self.head
        while x:
            print(x.data,end="->")
            x=x.next
    def find(self,n):
        c=0
        p=self.head
        while p:
            c=c+1
            if c==n:
                print(p.data)
            p=p.next
        

if __name__=="__main__":
    l=Linked()
    i=1
    while(i<10):
        l.insert(i)
        i=i+1
    l.printl()
    l.rev()
    print()
    n=int(input("enter node length to print from end"))
    l.find(n)
