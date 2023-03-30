class Node:
    def __init__(self, nodeValue=None):
        self.value = nodeValue
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        return '\n'.join([str(x.value) for x in self.linkedList])

    def isEmpty(self):
        return False if self.linkedList.head else True

    def push(self, value):
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node
        return "Element added!"

    def pop(self):
        if self.isEmpty():
            return "No element left to pop!"
        val = self.linkedList.head.value
        self.linkedList.head = self.linkedList.head.next
        return val

    def peek(self):
        return "Stack is empty!" if self.isEmpty() else self.linkedList.head.value

    def delete(self):
        self.linkedList.head = None


stack = Stack()
# print(stack.isEmpty())
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print('------------')
print(stack.pop())
print('------------')
print(stack.peek())
print("Deleting the entire stack")
stack.delete()
print(stack)
