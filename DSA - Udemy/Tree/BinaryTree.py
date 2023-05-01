import sys, os
sys.path.append("C:\\Python Practice\\DSA - Udemy\\Queue")
import QueueLinkedList as Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


binaryTree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
leftChild.leftChild = TreeNode("Tea")
leftChild.rightChild = TreeNode("Coffe")
rightChild = TreeNode("Cold")
binaryTree.leftChild = leftChild
binaryTree.rightChild = rightChild


def preOrderTraversal(rootNode):
    if not rootNode:
        return None
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
        customQueue = Queue.Queue()
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            print(root.data)
            if root.leftChild is not None:
                customQueue.enQueue(root.leftChild)
            if root.rightChild is not None:
                customQueue.enQueue(root.rightChild)


def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "Binary tree does not exist"
    else:
        customQueue = Queue.Queue()
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            if root.data == nodeValue:
                return "Value found!"
            if root.leftChild is not None:
                customQueue.enQueue(root.leftChild)
            if root.rightChild is not None:
                customQueue.enQueue(root.rightChild)
        return "Not found!"


def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = Queue.Queue()
        customQueue.enQueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.deQueue()
            if root.leftChild is not None:
                customQueue.enQueue(root.leftChild)
            else:
                root.leftChild = newNode
                return "Successfully Inserted"
            if root.rightChild is not None:
                customQueue.enQueue(root.rightChild)
            else:
                root.rightChild = newNode
                return "Successfully Inserted"


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        cQ = Queue.Queue()
        cQ.enQueue(rootNode)
        while not cQ.isEmpty():
            root = cQ.deQueue()
            if root.leftChild is not None:
                cQ.enQueue(root.leftChild)
            if root.rightChild is not None:
                cQ.enQueue(root.rightChild)
        return root


def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        cQ = Queue.Queue()
        cQ.enQueue(rootNode)
        while not cQ.isEmpty():
            root = cQ.deQueue()
            if root.data is dNode:
                root.data = None
                return
            if root.rightChild:
                if root.rightChild is dNode:
                    root.rightChild = None
                    return
                else:
                    cQ.enQueue(root.rightChild)
            if root.leftChild:
                if root.leftChild is dNode:
                    root.leftChild = None
                    return
                else:
                    cQ.enQueue(root.leftChild)


def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        cQ = Queue.Queue()
        cQ.enQueue(rootNode)
        while not cQ.isEmpty():
            root = cQ.deQueue()
            if root.data == node:
                dNode = getDeepestNode(rootNode)
                root.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if root.leftChild is not None:
                cQ.enQueue(root.leftChild)
            if root.rightChild is not None:
                cQ.enQueue(root.rightChild)
        return "Failed to delete"


def deleteBT(rootNode):
    rootNode.data, rootNode.leftChild, rootNode.rightChild = None, None, None
    return "The BT has been successfully deleted"


# preOrderTraversal(binaryTree)
# inOrderTraversal(binaryTree)
# postOrderTraversal(binaryTree)
# print(insertNodeBT(binaryTree, TreeNode("Cola")))
# levelOrderTraversal(binaryTree)
# print(searchBT(binaryTree, "Hot"))
# deleteNodeBT(binaryTree, "Hot")
deleteBT(binaryTree)
levelOrderTraversal(binaryTree)
