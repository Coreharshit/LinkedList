'''
N = 8

value[] = {1,2,2,1,2,0,2,2}

Output: 0 1 1 2 2 2 2 2

Explanation: All the 0s are segregated
to the left end of the linked list,
2s to the right end of the list, and
1s in between.
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
    def seg(self):
        int0=int1=int2=0
        p=self.head
        q=self.head
        while p:
            if p.data==0:
                int0=int0+1
            elif p.data==1:
                int1=int1+1
            elif p.data==2:
                int2=int2+1
            else:
                break
            p=p.next
        print(int0,int1,int2)
        while q:
            if (int0!=0):
                q.data=0
                int0=int0-1
            else:
                if (int1!=0):
                    q.data=1
                    int1=int1-1
                else:
                    if (int2!=0):
                        q.data=2
                        int2=int2-1
            q=q.next
            
        
if __name__=="__main__":
    l=Linked()
    l.insert(1)
    l.insert(2)
    l.insert(2)
    l.insert(1)
    l.insert(2)
    l.insert(0)
    l.insert(2)
    l.insert(2)
    
    l.printl()
    print()
    l.seg()
    l.printl()
