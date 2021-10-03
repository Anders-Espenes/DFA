from copy import deepcopy
from typing import List # Allow for typesetting lists
from node import Node
from DFA import DFA
class Apta:
    stack = []

    def __init__(self, alphabet, depth, root: Node = None):
        self.root = root
        self.alphabet = alphabet
        self.depth = depth

    def setRoot(self, root):
        self.root = root

    # Transitions throught the apta tree until it reaches a node and returns the node
    def input(self, input_string: str = "") -> Node:
        current_node = self.root
        for trans in input_string:
            # print(str(trans) + " ->", end=" ")
            if current_node.children:
                current_node = current_node.next(trans)
        return current_node

    def copy_tree(self):
        self.stack.append(deepcopy(self.root))

    def print(self):
        self.root.print_nodes([])

    def complete(self) -> bool:
        return self.root.check_if_label(alphabet=self.alphabet, unique=[])

    def pop_tail(self):
        self.root = self.stack[-1]
        self.stack.pop(-1)