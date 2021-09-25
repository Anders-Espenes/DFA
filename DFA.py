import itertools as it
from node import Node

class DFA:

	def __init__(self, trans, start: int, accepting, alphabet):
		self.alphabet = alphabet					# Allowed input values for transitions
		self.transitions = trans					# List Dictionaires showing allowed transitions
		self.start_state = start					# Starting entrypoint for the DFA
		self.accepting_state = accepting			# List of

	# Input traverses the DFA printing out the state of the ending node of the string
	def input(self, input_string: str = "") -> bool:
		state = self.start_state
		for trans in input_string:
			# print(str(trans) + " ->", end=" ")
			state = self.transitions[state][trans]
		return state in self.accepting_state

	# Generates all possible combinations of the alphabet in the DFA up to a given length
	def generate_all_strings(self, length: int, p: bool = False):
		string_results = []

		for i in range(0, length+1):
			all_string = it.product(self.alphabet, repeat=i)

			if p:
				print(f"Creating all string from alphabet, {self.alphabet}, up to length {i}")

			string_results.append([])

			# Handles all string up to length
			for s in all_string:
				string = "".join(map(str, s))
				string_results[i].append([string, self.input(string)])
				if p:
					print(f"String: {string}, result: {self.input(string)}")

		return string_results



