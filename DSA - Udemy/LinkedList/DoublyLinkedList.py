class Node:
    def __init__(self, value=None):
        self.prev = None
        self.value = value
        self.next = None


class DoublyLinkedList:
    def __init__(self, initialValue):
        node = Node(initialValue)
        node.next = node.prev = None
        self.head = self.tail = node

    def __iter__(self):
        node: Node = self.head
        while node:
            yield node
            node = node.next

    def insertDLL(self, nodeValue, position):
        if self.head is None:
            return "Double LinkedList is empty!"
        else:
            newNode = Node(nodeValue)
            if position == 0:
                newNode.next = self.head
                newNode.prev = None
                self.head.prev = newNode
                self.head = newNode
            elif position == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                index = 0
                currentNode = self.head
                while index < position - 1:
                    currentNode = currentNode.next
                    index += 1
                if currentNode == self.tail:
                    newNode.prev = currentNode
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                    self.tail = newNode
                else:
                    newNode.prev = currentNode
                    newNode.next = currentNode.next
                    newNode.next.prev = newNode
                    currentNode.next = newNode

    def traverseForwardDLL(self):
        if self.head is None:
            return "LinkedList is empty"
        node = self.head
        while node:
            print(node.value)
            node = node.next

    def traverseBackwardDLL(self):
        if self.head is None:
            return "LinkedList is empty"
        node = self.tail
        while node:
            print(node.value)
            node = node.prev

    def searchDLL(self, value):
        if self.head is None:
            return "LinkedList is empty"
        node = self.head
        while node:
            if node.value == value:
                return "Element found!"
            node = node.next
        return "Element not found!"

    def deleteDLL(self, position):
        if self.head is None:
            return "Nothing to delete from an empty LinkedList!"
        else:
            if self.head == self.tail:
                self.head = self.tail = None
                return [n.value for n in self]
            elif position == 0:
                self.head.next.prev = None
                self.head = self.head.next
                return [n.value for n in self]
            elif position == -1:
                self.tail.prev.next = None
                self.tail = self.tail.prev
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

    def deleteEntireDLL(self):
        node = self.head
        if node is None:
            return "LinkedList is empty!"
        while node:
            node.prev = None
            node = node.next
        self.head = self.tail = None
        return [n.value for n in self]


doublyLinkedList = DoublyLinkedList(0)
doublyLinkedList.insertDLL(1, -1)
doublyLinkedList.insertDLL(2, -1)
doublyLinkedList.insertDLL(3, 3)
doublyLinkedList.insertDLL(4, -1)
doublyLinkedList.insertDLL(5, -1)
print([node.value for node in doublyLinkedList])
# doublyLinkedList.traverseForwardDLL()
# doublyLinkedList.traverseBackwardDLL()
# print(doublyLinkedList.searchDLL(9))
# print(doublyLinkedList.deleteDLL(0))
print(doublyLinkedList.deleteEntireDLL())
