# Implement a Queue using two Stacks

class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()


class QueueViaStack:
    def __init__(self):
        self.inStack = Stack()
        self.outStack = Stack()

    def enQueue(self, item):
        self.inStack.push(item)

    def deQueue(self):
        while len(self.inStack):
            self.outStack.push(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.push(self.outStack.pop())
        return result


customQueue = QueueViaStack()
customQueue.enQueue(1)
customQueue.enQueue(2)
customQueue.enQueue(3)
customQueue.enQueue(4)
print(customQueue.deQueue())
customQueue.enQueue(5)
print(customQueue.deQueue())
