class Node:
    def __init__(self ,data):
        self.data = data
        self.left = None
        self.right = None

def isBST(node, leftNode, rightNode):
    if node is None:
        return True
    if node.data < leftNode or node.data > rightNode:
        return False
    return isBST(node.left, leftNode, node.data) and isBST(node.right, node.data, rightNode)
def is_bst_satisfied(root):
    if isBST(root, float('-inf'), float('inf')):
        print("True")
    else:
        print("False")
rootNode = Node(1)
rootNode.left = Node(2)
rootNode.right = Node(3)
rootNode.left.left = Node(4)
rootNode.right.right = Node(5)
print(is_bst_satisfied(rootNode))