'''
Input:

LinkedList = 12->15->10->11->5->6->2->3

Output: 15 11 6 3

Explanation: Since, 12, 10, 5 and 2 are
the elements which have greater elements
on the following nodes. So, after deleting
them, the linked list would like be 15,
11, 6, 3.
'''
'''
->concept reverse the link list kyuki last wle k right m kuch nhi hoga to vo del nhi ho sakta
->after traversing if data p>data p.next then p.next=p.next.next otherwise p=p.next reverse the end result and printit.
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
    def printl(self):
        x=self.head
        while x:
            print(x.data,end="->")
            x=x.next
    
    def reverse(self):
        prev=None
        Current=self.head
        while(Current is not None):
            next=Current.next
            Current.next=prev
            prev=Current
            Current=next
        self.head=prev
    def gtr_right(self):
        p=self.head
        while p.next:
            if p.data >p.next.data:
                p.next=p.next.next
            else:
                p=p.next
            
        

if __name__=="__main__":
    l=Linked()
    l.insert(12)
    l.insert(15)
    l.insert(10)
    l.insert(11)
    l.insert(5)
    l.insert(6)
    l.insert(2)
    l.insert(3)
    
    l.printl()
    print()
    l.reverse()
    print()
    l.gtr_right()
    l.printl()
    l.reverse()
    print()
    l.printl()
  
