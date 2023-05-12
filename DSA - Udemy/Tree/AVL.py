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


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disBalancedNode):
    newRoot = disBalancedNode.leftChild
    disBalancedNode.leftChild = disBalancedNode.leftChild.rightChild
    newRoot.rightChild = disBalancedNode
    disBalancedNode.height = 1 + max(getHeight(disBalancedNode.leftChild), getHeight(disBalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


def leftRotate(disBalancedNode):
    print(disBalancedNode.data, disBalancedNode.rightChild.data, disBalancedNode.rightChild.rightChild.data)
    newRoot = disBalancedNode.rightChild
    print(disBalancedNode.rightChild.leftChild)
    disBalancedNode.rightChild = disBalancedNode.rightChild.leftChild
    newRoot.leftChild = disBalancedNode
    disBalancedNode.height = 1 + max(getHeight(disBalancedNode.leftChild), getHeight(disBalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)


def insertNode(rootNode, nodeValue):
    if not rootNode:
        return AVLNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:     # LL Condition
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:     # LR Condition
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:   # RR Condition
        print('RR')
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:   # RL Condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 20)
levelOrderTraversal(newAVL)
