class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        return ' '.join([str(x) for x in self.items])

    def isEmpty(self):
        return True if self.items == [] else False

    def enQueue(self, value):
        self.items.append(value)
        return "The element is inserted"

    def deQueue(self):
        if self.isEmpty():
            return "Queue is empty!"
        return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Nothing to peek upon if the queue is empty!"
        return self.items[0]

    def delete(self):
        self.items.clear()


queue = Queue()
# print(queue.isEmpty())
queue.enQueue(1)
queue.enQueue(2)
queue.enQueue(3)
queue.enQueue(4)
# print(queue)
# print(queue.deQueue())
print(queue)
print(queue.peek())
print(queue.delete())
print(queue)
