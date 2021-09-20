import itertools as it
from node import Node

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

	def build_APTA(self, length: int):
		all_strings = self.generate_all_strings(length)

		# removed the first element that is the empty string
		# Pop pop since its a List[List[]]
		root_string = all_strings.pop(0).pop(0)

		root_node = Node(value=root_string[0], data="e", accepting=root_string[1])

		# adding nodes in breadth first
		for level in all_strings:
			for nodes in level:
				current_node = root_node
				for trans in nodes[0]:
					next_node = current_node.goto(trans)
					if next_node is None:
						current_node.setChild(Node(value=trans, data=nodes[0], accepting=nodes[1]))
					else:
						current_node = next_node
		root_node.print_nodes()
