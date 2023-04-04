# How would you design a stack which, in addition to push and pop, has a function min which
# returns the minimum element? Push, pop and min should all operate in O(1).

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        # if self.next:
        #     string += ', ' + str(self.next)
        return string


class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        if self.minNode:
            return self.minNode
        return None

    def push(self, item):
        if self.minNode and self.minNode.value < item:
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            self.minNode = Node(value=item, next=self.minNode)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value
        self.top = self.top.next
        return item


cS = Stack()
cS.push(2)
cS.push(3)
cS.push(4)
cS.push(1)
cS.push(5)
print(cS.min())
cS.pop()
cS.pop()
print(cS.min())
