class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def size_(node):
    if node is None:
        return 0
    else:
        return (size_(node.left) + 1 + size_(node.right))
rootNode = Node(1)
rootNode.left = Node(2)
rootNode.right = Node(3)
rootNode.left.left = Node(4)
rootNode.right.right = Node(5)
print(size_(rootNode))