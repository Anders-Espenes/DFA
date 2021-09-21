from DFA import DFA
from node import Node

def generateStrings():
	dfa_8 = DFA(
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

	dfa_10 = DFA(
		alphabet=['0', '1'],
		trans={1:  {'0': 7,  '1': 6},
			   2:  {'0': 10, '1': 7},
			   3:  {'0': 4,  '1': 4},
			   4:  {'0': 10, '1': 1},
			   5:  {'0': 9,  '1': 3},
			   6:  {'0': 6,  '1': 5},
			   7:  {'0': 7,  '1': 10},
			   8:  {'0': 2,  '1': 2},
			   9:  {'0': 9,  '1': 1},
			   10: {'0': 8,  '1': 4}},
		accepting=[5, 6, 7, 8],
		start=1
	)


	# dfa_8.build_prefix_tree(3)

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

	root_node.setChild(node0)
	root_node.setChild(node1)

	node0.setChild(node00)
	node0.setChild(node01)
	node1.setChild(node10)
	node1.setChild(node11)

	node00.setChild(node000)
	node00.setChild(node001)
	node01.setChild(node010)
	node01.setChild(node011)
	node10.setChild(node100)
	node10.setChild(node101)
	node11.setChild(node110)
	node11.setChild(node111)


	dfa_10.match_labels(root_node)






def greedy():
	pass


def backtracking():
	pass


def main():
	greedy()
	backtracking()


if __name__ == "__main__":
	main()
	generateStrings()
