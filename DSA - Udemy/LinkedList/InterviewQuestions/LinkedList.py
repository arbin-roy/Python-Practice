from random import randint


class Node:
    def __init__(self, nodeValue=None):
        self.prev = None
        self.value = nodeValue
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        return ' -> '.join([str(n.value) for n in self])

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        if self.head is None:
            newNode = Node(value)
            self.head = self.tail = newNode
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self
