


class Node:
    def __init__(self, node_data=None, next_node=None):
        self.data = node_data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, node_data):
        node = Node(node_data)
        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def insertNodeAtHead(self,llist, data):
        node = Node(data)
        node.next = llist
        return node
    
    def insertNodeAtPosition(head, data, position):
        n = head
        for _ in range(position - 1):
            n = n.next
        n_next = n.next
        n.next = SinglyLinkedListNode(data)
        n.next.next = n_next
        return head

    def printNode(self,head):
        while head:
            print(head.data)
            head = head.next
        return None

    def deleteNode(self,head,position):
        if position == 0:
            head = head.next
            return head
        direction = 0
        current = head
        while direction != position -1 :
            current = current.next
            direction += 1
        current.next = current.next.next
        return head
    

if __name__ == '__main__':
    llist_count = int(input())
    llist = SinglyLinkedList()
    tailData = [6,7,8,9]
    # Insert n nodes 
    for _ in range(llist_count):
        user_input = int(input())
        llist.insertNode(user_input)

    # Print all nodes 
    print('\n----------- Printing user input nodes -----------\n')
    llist.printNode(llist.head)
     
    # Insert n nodes at tail
    for tail in tailData:
        llist_head = llist.insertNodeAtHead(llist.head,tail)
        llist.head = llist_head
    
    # Print all nodes 
    print('\n----------- Printing inserted node at head  -----------\n')
    llist.printNode(llist.head)
    
    # Insert data at a given position
    for tail in tailData:
        llist = llist.insertNodeAtPosition(head=llist.head ,data=tail,position = 1)
    
    # Print all nodes 
    print('\n----------- Printing inserted node at head  -----------\n')
    llist.printNode(llist.head)
    
    print('\n----------- Delete node at position 2 -----------\n')
    # Delete a speific node 
    deleted = llist.deleteNode(llist.head,2)
    llist.printNode(deleted)
