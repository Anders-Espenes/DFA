from typing import List # Allow for typesetting lists
from node import Node
from DFA import DFA
class Apta:
    def __init__(self, root: Node = None):
        self.root = root

    def setRoot(self, root):
        self.root = root

    # Transitions throught the apta tree until it reaches a node and returns the node
    def input(self, input_string: str = "") -> Node:
        current_node = self.root
        for trans in input_string:
            # print(str(trans) + " ->", end=" ")
            current_node = current_node.next(trans)
        return current_node

    def print(self):
        self.root.print_nodes([])

    def get_depth(self, node: Node, i: int = 0) -> int:
        if node.children:
            count = i + 1
            return self.get_depth(node.children[0], count)
        else:
            return i
