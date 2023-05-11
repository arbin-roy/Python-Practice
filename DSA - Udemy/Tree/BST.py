import sys
sys.path.append("C:\\Python Practice\\DSA - Udemy\\Queue")
import QueueLinkedList as Queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


def insertNode(rootNode, nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "Node successfully inserted"


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


def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode


def deleteEntireBST(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST is deleted"


newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))
# print(newBST.data, newBST.leftChild.data, newBST.rightChild.data)
# preOrderTraversal(newBST)
# inOrderTraversal(newBST)
# postOrderTraversal(newBST)
# levelOrderTraversal(newBST)
# searchNode(newBST, 90)
# deleteNode(newBST, 60)
print(deleteEntireBST(newBST))
levelOrderTraversal(newBST)
