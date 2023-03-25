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

    def traverseForwardCDLL(self):
        if self.head is None:
            return "LinkedList is empty!"
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.head:
                break
        return 0

    def traverseBackwardCDLL(self):
        if self.head is None:
            return "LinkedList is empty!"
        node = self.tail
        while node:
            print(node.value)
            node = node.prev
            if node == self.tail:
                break
        return 0

    def searchCDLL(self, searchValue):
        if self.head is None:
            return "LinkedList is empty!"
        node = self.head
        while node:
            if node.value == searchValue:
                return "Value found!"
            if node.next == self.head:
                return "404"
            node = node.next

    def deleteCDLL(self, position):
        if self.head is None:
            return "LinkedList is empty!"
        else:
            if self.head == self.tail:
                self.head.prev = self.head.next = None
                self.head = self.tail = None
                return [n.value for n in self]
            elif position == 0:
                node = self.head
                node.next.prev = self.tail
                self.head = node.next
                self.tail.next = self.head
                return [n.value for n in self]
            elif position == -1:
                node = self.tail
                node.prev.next = self.head
                self.tail = node.prev
                self.head.prev = self.tail
                return [n.value for n in self]
            else:
                node = self.head
                index = 0
                while index < position - 1:
                    node = node.next
                    index += 1
                node.next = node.next.next
                node.next.prev = node
                return [n.value for n in self]

    def deleteEntireCDLL(self):
        if self.head is None:
            return "Nothing to delete if the list is empty!"
        else:
            self.tail.next = None
            node = self.head
            while node:
                node.prev = None
                node = node.next
            self.head = self.tail = None
            return [n.value for n in self]


circularDoublyLinkedList = CircularDoublyLinkedList(0)
circularDoublyLinkedList.insertCDLL(1, -1)
circularDoublyLinkedList.insertCDLL(2, -1)
circularDoublyLinkedList.insertCDLL(3, -1)
circularDoublyLinkedList.insertCDLL(4, -1)
circularDoublyLinkedList.insertCDLL(5, -1)
print([n.value for n in circularDoublyLinkedList])
# circularDoublyLinkedList.traverseForwardCDLL()
# circularDoublyLinkedList.traverseBackwardCDLL()
# print(circularDoublyLinkedList.searchCDLL(6))
# print(circularDoublyLinkedList.deleteCDLL(7))
print(circularDoublyLinkedList.deleteEntireCDLL())
