from copy import deepcopy
from math import atan
from typing import List
from DFA import DFA
from node import Node
from apta import Apta
from utility import generate_strings, generate_test_strings


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
def build_prefix_tree_temp(all_strings) -> Apta:

	# removed the first element that is the empty string
	# Pop pop since its a List[List[]]
	root_string = all_strings.pop(0).pop(0)

	root_node = Node(data="e", accepting=root_string[1])

	# adding nodes in breadth first
	for level in all_strings:
		for nodes in level:
			current_node = root_node
			for trans in nodes[0]:
				next_node = current_node.transition(trans)
				if next_node is None:
					current_node.addChild(
						Node(data=nodes[0], accepting=nodes[1]))
				else:
					current_node = next_node
	return Apta(root_node)	# Returns the root node of the tree



def build_prefix_tree(strings: List, dfa: DFA, root=Node(data="")):
	for string in strings:
		current_node = root
		for char in string:
			temp = current_node.transition(char)
			if temp is None:
				current_node.addChild(Node(value=char, data=current_node.data+char))
			current_node = current_node.transition(char)
		current_node.accepting = dfa.input(string)
	return root


# TODO: Clean this up a bit
def match_labels(root: Node, child: Node, temp=True) -> bool:
	if (root.accepting == child.accepting or root.accepting==None or child.accepting==None):
		if (len(root.children) != 0) and (len(child.children) != 0):	# Check if both nodes still have children to compare
			for child1, child2 in zip(root.children,child.children): 	# Compare two and two children
				# Check if both children have the same label
				if(child1.accepting == child2.accepting or child1.accepting == None or child2.accepting == None):
					temp = match_labels(child1, child2, temp)			# Check if the childrens children have the same label
				else: return False										# A child node did not have the same label
	else: return False
	return temp

def merge_states(root: Node, child: Node, target: Node):
	root.setChild(child, target)
	child.destroy()


def test(dfa: DFA, apta: Apta, nr_of_strings, alphabet, depth) -> bool:
	try:
		for s in generate_test_strings(nr_of_strings, alphabet, depth):
			# print(s)
			if dfa.input(s) != apta.input(s).accepting:
				print("Something is wrong!")
				return False
		print("Sucess")
		return True
	except:
		print("Transition was not valid")	# Path does not exists for the given input string
		return False




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


def backtracking(apta: Apta, unique = []):
	"""
		Similar to greedy
		Attempt to match labels
		If a match is found, copy the tree and merge the nodes
		Continue until there are no nodes in tree that are not unique
		See if the tree is complete, check if every node has labels, if not assign label at random
		Test if the tree is correct, if not backtrack, pop tree from list
	"""
	# print(unique)
	if(len(unique) == 0):
		unique.append(apta.root)
	
	# Check if finished
	if apta.complete() == True:
		return
	# Check promising
	for root in unique:
		if root.children:
			for child in root.children:
				if child not in unique:
					for node in unique:
						if match_labels(child, node):
							temp_node = deepcopy(node)
							merge_states(root, child, node)
							backtracking(apta, list(unique))
							node = temp_node
						else: unique.append(child)
	return
	# if current_node.children:
		# for child in current_node.children:
			# for node in unique:
				# if match_labels(child, node):
					# apta.copy_tree()
					# merge_states(current_node, child, node)
					# backtracking(apta, apta.get_unique(unique))
			# unique.append(child)
			# backtracking(apta, child)


def task_2():
	depth = 8
	alphabet = 2
	nr_of_strings = 1000

	# Comment what DFA you want
	dfa = dfa_eight()
	# dfa = dfa_ten()

	# Build the apta tree
	apta = Apta(alphabet=alphabet, depth=depth)
	apta.setRoot(build_prefix_tree(dfa.generate_strings(depth), dfa))

	# Perform the greedy algorithm
	greedy(apta.root)
	apta.print()
	# Generate test strings and see if the apta tree is correct
	test(dfa, apta, nr_of_strings, alphabet, depth)

def task_3():
	depth = 8
	alphabet = 1
	nr_of_strings = 5

	# Set dfa, same as before
	# dfa = dfa_eight()
	dfa = dfa_ten()

	
	# Generate apta tree
	apta = Apta(alphabet=alphabet, depth=depth)
	apta.setRoot(build_prefix_tree(generate_strings(nr_of_strings, alphabet, depth), dfa))	# Testing
	# apta = build_prefix_tree(generate_strings(1000, 1, 10), dfa)	# Oppgave 
	# apta = build_prefix_tree(generate_strings(1000, 1, 100), dfa)
	# apta = build_prefix_tree(generate_strings(1000, 1, 1000), dfa)

	# Run the backtracking
	backtracking(apta)
	apta.print()
	test(dfa, apta, nr_of_strings, alphabet, depth)

def main():
	task_2()
	# task_3()

if __name__ == "__main__":
	main()
