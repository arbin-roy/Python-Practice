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


# preOrderTraversal(binaryTree)
# inOrderTraversal(binaryTree)
postOrderTraversal(binaryTree)
