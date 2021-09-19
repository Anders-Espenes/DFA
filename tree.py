from node import Node
class tree:
    def __init__(self):
        self.root = None

    def setRoot(self, root):
        self.root = root


    def addChildren(self, node, left, right):
        node.setLeftChild(left)
        node.setRightChild(right)

    