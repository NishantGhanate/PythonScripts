

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def print_doubly_linked_list(self,node, sep, fptr):
        while node:
            print(node.data)
            node = node.next
 
    # DoublyLinkedListNode:
    #     int data
    #     DoublyLinkedListNode next
    #     DoublyLinkedListNode prev

    def reverse(self,head):
        curr = new_head = head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            new_head = curr
            curr = curr.prev
        return new_head

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        llist1 = llist.reverse(llist.head)
        llist.print_doubly_linked_list(llist1)
        # print_doubly_linked_list(llist1, ' ', fptr)
    