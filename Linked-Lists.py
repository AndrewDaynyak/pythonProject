class Node:
    def __init__(self, value, next=None):
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def insert(self, value):
        node=Node(value)
        if self.head is None:
            self.head=node
            return
        current_node=self.head
        while True:
            if current_node.next is None:
                current_node.next=node
                break
            current_node=current_node.next

    def printl(self):
        current_node=self.head
        while current_node is not None:
            print(current_node.value, '->', end='')
            current_node=current_node.next
        print('None')
ll=LinkedList()
ll.insert('44')
ll.insert('11')
ll.insert('24')
ll.insert('46')
ll.printl()