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
                newNode.prev = currentNode
                newNode.next = currentNode.next
                print(newNode.next)
                print('hui')


doublyLinkedList = DoublyLinkedList(0)
print([node.value for node in doublyLinkedList])
doublyLinkedList.insertDLL(1, -1)
doublyLinkedList.insertDLL(2, -1)
doublyLinkedList.insertDLL(3, -1)
doublyLinkedList.insertDLL(4, -1)
doublyLinkedList.insertDLL(5, -1)
print([node.value for node in doublyLinkedList])
