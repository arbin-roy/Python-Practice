import sys
sys.path.append("C:\\Python Practice\\DSA - Udemy\\Queue")
import QueueLinkedList as Queue


class AVLNode:
    def __init__(self, nodeValue):
        self.data = nodeValue
        self.leftChild = None
        self.rightChild = None
        self.height = 1


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)


def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)


def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)


def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        cQ = Queue.Queue()
        cQ.enQueue(rootNode)
        while not cQ.isEmpty():
            root = cQ.deQueue()
            print(root.data)
            if root.leftChild is not None:
                cQ.enQueue(root.leftChild)
            if root.rightChild is not None:
                cQ.enQueue(root.rightChild)


def searchNode(rootNode, nodeValue):
    try:
        if rootNode.data == nodeValue:
            print("The value is found")
        elif nodeValue < rootNode.data:
            searchNode(rootNode.leftChild, nodeValue)
        else:
            searchNode(rootNode.rightChild, nodeValue)
    except AttributeError:
        print("The value not found")


newAVL = AVLNode(10)
