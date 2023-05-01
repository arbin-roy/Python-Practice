class Node:
    def __init__(self, nodeValue=None):
        self.value = nodeValue
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def __iter__(self):
        curNode = self.front
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        return " ".join([str(x) for x in self.linkedList])

    def isEmpty(self):
        return False if self.linkedList.front else True

    def enQueue(self, value):
        node = Node(value)
        if self.linkedList.front is None:
            self.linkedList.front = self.linkedList.rear = node
        else:
            self.linkedList.rear.next = node
            self.linkedList.rear = node

    def deQueue(self):
        if self.isEmpty():
            return "Queue is empty!"
        else:
            val = self.linkedList.front.value
            if self.linkedList.front == self.linkedList.rear:
                self.linkedList.front = self.linkedList.rear = None
            else:
                self.linkedList.front = self.linkedList.front.next
            return val

    def peek(self):
        return "Queue is empty!" if self.isEmpty() else self.linkedList.front

    def delete(self):
        self.linkedList.front = self.linkedList.rear = None
        return "Queue deleted!"


# queue = Queue()
# queue.enQueue(1)
# queue.enQueue(2)
# queue.enQueue(3)
# queue.enQueue(4)
# print(queue)
# print(queue.deQueue())
# print(queue.delete())
# print(queue)
# print(queue.peek())
