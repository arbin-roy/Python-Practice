class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = self.tail = node

    def __iter__(self):
        node: Node = self.head
        while node:
            yield node
            if node == self.tail:
                break
            node = node.next

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = self.tail = node
        return "The CSLL has been created"

    def insertCSLL(self, nodeValue, position):
        if self.head is None:
            return "Linked List is empty!"
        elif position == 0:
            newNode = Node(nodeValue)
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
            return "Value inserted at the first position"
        elif position == -1:
            newNode = Node(nodeValue)
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
            return "Value inserted at the last"
        else:
            newNode, prevNode = Node(nodeValue), self.head
            index = 0
            while index < position - 1:
                if prevNode.next == self.head:
                    return "Position should be in LinkedList's item range"
                prevNode = prevNode.next
                index += 1
            newNode.next = prevNode.next
            prevNode.next = newNode
            if newNode.next == self.head:
                self.tail = newNode
            return f"Value inserted at position: {position}"

    def traverseCSll(self):
        if self.head is None:
            return "Linked List is empty!"
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break

    def searchCSLL(self, value):
        if self.head is None:
            return "Linked List is empty!"
        node = self.head
        while node:
            if node.value == value:
                return "Element found!"
            node = node.next
            if node == self.tail.next:
                return "Element not found"

    def deleteCSLL(self,  position):
        if self.head is None:
            return "Nothing to delete when LinkedList is empty!"
        elif position == 0:
            if self.head == self.tail:
                self.head = self.tail.next = self.tail = None
                return [node.value for node in self]
            else:
                self.head = self.head.next
                self.tail.next = self.head
                print(self.head.value, self.tail.value)
                return [node.value for node in self]
        elif position == -1:
            if self.head == self.tail:
                self.head = self.tail.next = self.tail = None
                return [node.value for node in self]
            else:
                currentNode = self.head
                while currentNode:
                    if currentNode.next == self.tail:
                        break
                    currentNode = currentNode.next
                currentNode.next = self.tail
                self.tail = currentNode
                print(self.head.value, self.tail.value)
                return [node.value for node in self]
        else:
            currentNode = self.head
            index = 0
            while index < position - 1:
                if currentNode.next == self.head:
                    return "Node does not exist in the list!"
                currentNode = currentNode.next
                index += 1
            currentNode.next = currentNode.next.next
            if currentNode.next == self.tail.next:
                self.tail = currentNode
            print(self.head.value, self.tail.value)
            return [node.value for node in self]

    def deleteEntireCSLL(self):
        if self.head is None:
            return "LinkedList is empty!"
        self.head = self.tail.next = self.tail = None
        return [node.value for node in self]


circularSinglyLinkedList = CircularSinglyLinkedList(0)
# print(circularSinglyLinkedList.createCSLL(0))
print(circularSinglyLinkedList.insertCSLL(1, -1))
print(circularSinglyLinkedList.insertCSLL(2, -1))
print(circularSinglyLinkedList.insertCSLL(3, 3))
print(circularSinglyLinkedList.insertCSLL(4, -1))
print(circularSinglyLinkedList.insertCSLL(5, 5))

print([node.value for node in circularSinglyLinkedList])
# circularSinglyLinkedList.traverseCSll()
# print(circularSinglyLinkedList.searchCSLL(8))
# print(circularSinglyLinkedList.deleteCSLL(9))
print(circularSinglyLinkedList.deleteEntireCSLL())
