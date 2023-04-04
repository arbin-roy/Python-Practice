# Use a single list to implement three stacks

class MultiStack:
    def __init__(self, stackSize):
        self.numberStacks = 3
        self.custList = [0] * (stackSize * self.numberStacks)
        self.sizes = [0] * self.numberStacks
        self.stackSize = stackSize

    def isFull(self, stackNum):
        return True if self.sizes[stackNum] == self.stackSize else False

    def isEmpty(self, stackNum):
        return True if self.sizes[stackNum] == 0 else False

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackSize
        return offset + self.sizes[stackNum] - 1

    def push(self, item, stackNum):
        if self.isFull(stackNum):
            return "Stack is full!"
        else:
            self.sizes[stackNum] += 1
            self.custList[self.indexOfTop(stackNum)] = item
            return "Element inserted"

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return "Stack is empty"
        else:
            value = self.custList[self.indexOfTop(stackNum)]
            self.custList[self.indexOfTop(stackNum)] = 0
            self.sizes[stackNum] -= 1
            return value

    def peek(self, stackNum):
        return "Stack is empty" if self.isEmpty(stackNum) else self.custList[self.indexOfTop(stackNum)]


customStack = MultiStack(6)
customStack.push(1, 0)
customStack.push(1, 1)
customStack.push(2, 1)
customStack.push(1, 2)
print(customStack.custList)
