from copy import deepcopy
from typing import List # Allow for typesetting lists
from node import Node
from DFA import DFA
class Apta:
    stack = []

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

    def copy_tree(self):
        self.stack.append(deepcopy(self.root))

    def print(self):
        self.root.print_nodes([])

    def pop_tail(self):
        self.stack.pop(-1)

    