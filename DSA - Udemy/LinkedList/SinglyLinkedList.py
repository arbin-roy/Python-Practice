class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node: Node = self.head
        while node:
            yield node
            node = node.next

    # Inserting value into Singly Linked List
    def insertSLL(self, value, position):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if position == 0:
                newNode.next = self.head
                self.head = newNode
            elif position == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < position - 1:
                    if tempNode.next is None:
                        return "Position should be in LinkedList's item range"
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    # Traversing values in Singly Linked List
    def traverseSLL(self):
        start = self.head
        if start is None:
            print("LinkedList is empty!")
        else:
            while start is not None:
                print(start.value)
                start = start.next

    # Searching values in Singly Linked List
    def searchSLL(self, searchValue: int):
        start = self.head
        if start is None:
            return "LinkedList is empty!"
        else:
            while start is not None:
                if start.value == searchValue:
                    return f"{searchValue} is present"
                start = start.next
            return f"{searchValue} is not present"

    # Deleting nodes in Singly Linked List
    def deleteSLL(self, position):
        if self.head is None:
            return "LinkedList is empty!"
        elif position == 0:
            if self.head == self.tail:
                self.head = self.tail = None
                return [node.value for node in self]
            else:
                self.head = self.head.next
                return [node.value for node in self]
        elif position == -1:
            if self.head == self.tail:
                self.head = self.tail = None
                return [node.value for node in self]
            else:
                currentNode = self.head
                while currentNode:
                    if currentNode.next == self.tail:
                        break
                    currentNode = currentNode.next
                currentNode.next = None
                self.tail = currentNode
                return [node.value for node in self]
        else:
            prevNode = self.head
            index = 0
            while index < position - 1:
                index += 1
                if prevNode.next is None:
                    return "Position should be in LinkedList's item range"
                prevNode = prevNode.next
            prevNode.next = prevNode.next.next
            return [node.value for node in self]

    def deleteEntireSLL(self):
        if self.head is None:
            return "LinkedList is empty!"
        else:
            self.head = self.tail = None
            return [node.value for node in self]


singlyLinkedList = SinglyLinkedList()
singlyLinkedList.insertSLL(1, 0)
singlyLinkedList.insertSLL(2, -1)
singlyLinkedList.insertSLL(3, -1)
singlyLinkedList.insertSLL(4, 2)
singlyLinkedList.insertSLL(0, 0)

print([node.value for node in singlyLinkedList])
# singlyLinkedList.traverseSLL()
# print(singlyLinkedList.searchSLL(3))
# print(singlyLinkedList.deleteSLL(-1))
print(singlyLinkedList.deleteEntireSLL())
