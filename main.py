import functools
import itertools as it
import operator


class DFA:
	def __init__(self, trans, start: int, accepting, alphabet):
		self.alphabet = alphabet
		self.transitions = trans
		self.start_state = start
		self.accepting_state = accepting

	def input(self, input_string: str = "") -> bool:
		state = self.start_state
		for trans in input_string:
			state = self.transitions[state][trans]

		return state in self.accepting_state

	def generate_all_strings(self, length: int, p: bool = False):
		string_results = []

		all_string = it.product(self.alphabet, repeat=length)

		# Handling the first string, which is empty
		all_string.__next__()
		if p:
			print(f"Creating all string from alphabet, {self.alphabet}, up to length {length}")
			print(f"String: e, result: {self.input()}")
		string_results.append(["e", self.input()])

		# Handles all string up to length
		for s in all_string:
			string = "".join(map(str, s)).lstrip("0")
			string_results.append([string, self.input(string)])
			if p:
				print(f"String: {string}, result: {self.input(string)}")

		return string_results


def generateStrings():
	dfa_10 = DFA(
		alphabet=['0', '1'],
		trans={1: {'0': 6, '1': 7},
			   2: {'0': 10, '1': 7},
			   3: {'0': 4, '1': 4},
			   4: {'0': 10, '1': 1},
			   5: {'0': 9, '1': 3},
			   6: {'0': 6, '1': 5},
			   7: {'0': 7, '1': 10},
			   8: {'0': 2, '1': 2},
			   9: {'0': 9, '1': 1},
			   10: {'0': 8, '1': 4}},
		accepting=[5, 6, 7, 8],
		start=1
	)

	dfa_10.generate_all_strings(3, True)

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

	dfa_8.generate_all_strings(3, True)


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
