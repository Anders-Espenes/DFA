import itertools as it

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