# This is also and example of circular queue

class Queue:
    def __init__(self, size):
        self.items = size * [None]
        self.maxSize = size
        self.start = -1
        self.top = -1

    def __str__(self):
        return ' '.join([str(x) for x in self.items])

    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        return True if self.top == -1 else False

    def enQueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of the Queue"

    def deQueue(self):
        if self.isEmpty():
            return "The Queue is empty!"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement

    def peek(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.start = self.top = -1


queue = Queue(4)
# print(queue.isFull())
# print(queue.isEmpty())
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.enQueue(4)
# print(queue.deQueue())
queue.delete()
print(queue)
# print(queue.peek())
