class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None

class Doubly:
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            new_node.prev = None
            return
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def printi(self):
        p = self.head
        while p:
            print(p.data, end="<->")
            p = p.next
        print()

    def reverseDoubly(self):
        current = self.head
        temp = None
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        
        # After the loop, temp will be pointing to the new head node's prev (which is None)
        if temp is not None:
            self.head = temp.prev

if __name__ == "__main__":
    q = Doubly()
    q.insert_at_end(4)
    q.insert_at_end(5)
    q.insert_at_end(2)
    print("Original list:")
    q.printi()
    
    q.reverseDoubly()
    print("Reversed list:")
    q.printi()
