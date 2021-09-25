from DFA import DFA
from node import Node
from apta import Apta
from utility import generate_strings


def test_Apta() -> Node:
	root_node = Node("", "e", False)

	node0 = Node("0", "0", False)
	node1 = Node("1", "1", True)

	node00 = Node("0", "00", False)
	node01 = Node("1", "01", True)
	node10 = Node("0", "10", True)
	node11 = Node("1", "11", False)

	node000 = Node("0", "000", False)
	node001 = Node("1", "001", True)
	node010 = Node("0", "010", True)
	node011 = Node("1", "011", False)
	node111 = Node("1", "111", True)
	node110 = Node("0", "110", False)
	node101 = Node("1", "101", False)
	node100 = Node("0", "100", True)

	root_node.addChild(node0)
	root_node.addChild(node1)

	node0.addChild(node00)
	node0.addChild(node01)
	node1.addChild(node10)
	node1.addChild(node11)

	node00.addChild(node000)
	node00.addChild(node001)
	node01.addChild(node010)
	node01.addChild(node011)
	node10.addChild(node100)
	node10.addChild(node101)
	node11.addChild(node110)
	node11.addChild(node111)

	return root_node


def dfa_eight():
	return DFA(
		alphabet=['0', '1', '2'],
		trans={1: {'0': 3,  '1': 5, '2': 2},
                    2: {'0': 4,  '1': 1, '2': 6},
                    3: {'0': 1,  '1': 4, '2': 7},
                    4: {'0': 2,  '1': 8, '2': 3},
                    5: {'0': 7,  '1': 1, '2': 6},
                    6: {'0': 8,  '1': 5, '2': 2},
                    7: {'0': 5,  '1': 8, '2': 3},
                    8: {'0': 6,  '1': 4, '2': 7}},
		accepting=[1],
		start=1
	)


def dfa_ten():
	return DFA(
		alphabet=['0', '1'],
		trans={1:  {'0': 6,  '1': 7},
                    2:  {'0': 7, '1': 10},
                    3:  {'0': 4,  '1': 4},
                    4:  {'0': 1, '1': 10},
                    5:  {'0': 3,  '1': 9},
                    6:  {'0': 6,  '1': 5},
                    7:  {'0': 7,  '1': 10},
                    8:  {'0': 2,  '1': 2},
                    9:  {'0': 1,  '1': 9},
                    10: {'0': 4,  '1': 8}},
		accepting=[5, 6, 7, 8],
		start=1
	)


# Check if every node have corresponding labels
def build_prefix_tree(dfa: DFA, length: int) -> Apta:
	all_strings = dfa.generate_all_strings(length)

	# removed the first element that is the empty string
	# Pop pop since its a List[List[]]
	root_string = all_strings.pop(0).pop(0)

	root_node = Node(value=root_string[0], data="e", accepting=root_string[1])

	# adding nodes in breadth first
	for level in all_strings:
		for nodes in level:
			current_node = root_node
			for trans in nodes[0]:
				next_node = current_node.transition(trans)
				if next_node is None:
					current_node.addChild(
						Node(value=trans, data=nodes[0], accepting=nodes[1]))
				else:
					current_node = next_node
	return Apta(root_node)	# Returns the root node of the tree


# TODO: Clean this up a bit
def match_labels(root: Node, child: Node, temp=True) -> bool:
	if (root.accepting == child.accepting):
		if (len(root.children) != 0) and (len(child.children) != 0):	# Check if both nodes still have children to compare
			for child1, child2 in zip(root.children,child.children): 	# Compare two and two children
				if(child1.accepting == child2.accepting):				# Check if both children have the same label
					temp = match_labels(child1, child2, temp)			# Check if the childrens children have the same label
				else: return False										# A child node did not have the same label
	else: return False
	return temp

def merge_states(root: Node, child: Node, target: Node):
	root.setChild(child, target)
	child.destroy()



def greedy(startNode: Node, unique = []):
	"""
	For every node in the tree, check if it is unique compared to prevously visited nodes.
	If NOT unique merge the node with node checking against.
	If unique add to list of unique
	"""

	if (len(unique) == 0):
		unique.append(startNode)
	for root in unique:	
		if root.children:	# Check if given root has children
			for child in root.children:		# Check if any children can merge with the current uniques
				isUnique = True				# Becomes false if a node is able to merge
				for node in unique:			# Test if any children can merge with any of the unique nodes
					if match_labels(child, node):	# Match labels between two nodes
						merge_states(root, child, node)	# Merge the nodes
						isUnique = False	# Could merge nodes
				if isUnique:				# No child where able to merge with a unique node, it is therefore a unique node
					unique.append(child)  # Could not merge nodes, node is unique


def backtracking():
	pass

def test(dfa: DFA, apta: Apta ) -> bool:
	for s in generate_strings(1000, 1, 3):
		if dfa.input(s) != apta.input(s).accepting:
			print("Something is wrong!")
			return False
	print("Sucess")
	return True


def main():
	depth = 3
	dfa = dfa_eight()
	# dfa = dfa_ten()
	apta = build_prefix_tree(dfa, depth)
	greedy(apta.root)
	apta.print()
	test(dfa, apta)
	
if __name__ == "__main__":
	main()
