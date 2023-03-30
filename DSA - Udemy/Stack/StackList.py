class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        return True if self.list == [] else False

    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"

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


stack = Stack()
print(stack.push(1))
print(stack.push(2))
print(stack.push(3))
print(stack.push(4))
# print(stack)
# print(stack.pop())
# print(stack.peek())
print(stack)
print(stack.delete())
print(stack)
