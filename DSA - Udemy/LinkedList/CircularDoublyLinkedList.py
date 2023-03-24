class Node:
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self, initialValue):
        node = Node(initialValue)
        node.next = node.prev = node
        self.head = self.tail = node

    def __iter__(self):
        node: Node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def insertCDLL(self, nodeValue, position):
        if self.head is None:
            print("LinkedList is empty!")
        else:
            newNode = Node(nodeValue)
            if position == 0:
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif position == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
                self.head.prev = self.tail
            else:
                index = 0
                tempNode = self.head
                while index < position - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.prev = tempNode
                newNode.next = tempNode.next
                tempNode.next.prev = newNode
                tempNode.next = newNode


circularDoublyLinkedList = CircularDoublyLinkedList(0)
circularDoublyLinkedList.insertCDLL(1, -1)
circularDoublyLinkedList.insertCDLL(2, -1)
circularDoublyLinkedList.insertCDLL(3, -1)
circularDoublyLinkedList.insertCDLL(4, -1)
circularDoublyLinkedList.insertCDLL(5, -1)
print([n.value for n in circularDoublyLinkedList])
print(circularDoublyLinkedList.tail.value)
