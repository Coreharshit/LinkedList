class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            p = self.head
            while p.next:
                p = p.next
            p.next = Node(value)

    def printit(self):
        p = self.head
        while p:
            print(p.data, end="->")
            p = p.next
        print("None")

    def segregate(self):
        if self.head is None:
            return

        # Initialize pointers for the even and odd lists
        even_head = even_tail = None
        odd_head = odd_tail = None

        current = self.head

        while current:
            if current.data % 2 == 0:
                if even_head is None:
                    even_head = even_tail = current
                else:
                    even_tail.next = current
                    even_tail = even_tail.next
            else:
                if odd_head is None:
                    odd_head = odd_tail = current
                else:
                    odd_tail.next = current
                    odd_tail = odd_tail.next

            current = current.next

        # If either even list or odd list is empty, no need to merge
        if even_tail is not None:
            even_tail.next = odd_head
        if odd_tail is not None:
            odd_tail.next = None

        # Update head to the head of the even list if it exists,
        # otherwise to the head of the odd list
        self.head = even_head if even_head else odd_head

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(17)
    ll.insert(15)
    ll.insert(8)
    ll.insert(9)
    ll.insert(2)
    ll.insert(4)
    ll.insert(6)
    print("Original list:")
    ll.printit()
    ll.segregate()
    print("Segregated list:")
    ll.printit()
