from typing import List # Allow for typesetting lists
from node import Node
from DFA import DFA
class Apta:
    def __init__(self, root: Node = None):
        self.root = root
        self.unique = []

    def setRoot(self, root):
        self.root = root


    # Transitions throught the apta tree until it reaches a node and returns the node
    def input(self, input_string: str = "") -> Node:
        current_node = self.root
        for trans in input_string:
            current_node = current_node.transition(trans)
        return current_node

    def print(self):
        self.root.print_nodes()


	# Get depth of child
	# Generate? all strings from alphabet for depth length
	# use strings/transitions generated and compere result from child and parent
	# If all strings give the same result, replace child with parent
	# else try next child
	# Call same function on children, that is != itself
    def get_depth(self, node: Node, i: int = 0) -> int:
        if node.children:
            count = i + 1
            return self.get_depth(node.children[0], count)
        else:
            return i

    def match_labels(self, dfa: DFA, root_node: Node):
        for child in root_node.children:
            depth = self.get_depth(child)
            
            transitions = dfa.generate_all_strings(depth).pop()
            print(f"depth: {depth}")
            print(f"transitions: {transitions}")
            print("")
            if root_node.accepting == child.accepting:
                for nodes in transitions:
                    new_root = root_node
                    new_child = child
                    print(f"looking at transitions: {nodes[0]}")
                    for trans in nodes[0]:
                        new_root = new_root.transition(trans)
                        print(f"new root: {new_root}")
                        new_child = new_child.transition(trans)
                        print(f"new child: {new_child}")

                        if new_root.accepting != new_child.accepting:
                            # Må komme ut av denne og forrige loop, for å se på neste child
                            print("aaaaaaahhhhh")
                    print("")
            else:
                print("nodes not ==")
                continue

		# Hvis vi kommer hit skal alle nodes være like så vi merger på en måte
