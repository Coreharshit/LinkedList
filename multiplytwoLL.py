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
    def val(self):
        p=""
        s=self.head
        while s:
            p=p+str(s.data)
            s=s.next
        return int(p)
if __name__=="__main__":
    l=Linked()
    m=Linked()
    i=1
    while(i<3):
        l.insert(i)
        i=i+1
    j=2
    while(j<4):
        m.insert(j)
        j=j+1
    k=l.val()
    w=m.val()
    print(k*w)
