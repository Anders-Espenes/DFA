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


	dfa_8.build_APTA(10)


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
