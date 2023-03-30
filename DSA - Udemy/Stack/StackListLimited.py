class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        return True if self.list == [] else False

    def isFull(self):
        return True if len(self.list) == self.maxSize else False

    def push(self, value):
        if self.isFull():
            return "The stack is full"
        self.list.append(value)
        return "Element added!"

    def pop(self):
        if self.isEmpty():
            return "No elements left to pop"
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "No elements left to pop"
        return self.list[-1]

    def delete(self):
        self.list.clear()
        return "Stack deleted!"


stack = Stack(4)
print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.push(5))
print(stack.isFull())
