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

	def build_prefix_tree(self, length: int):
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
					next_node = current_node.transition(trans)
					if next_node is None:
						current_node.setChild(Node(value=trans, data=nodes[0], accepting=nodes[1]))
					else:
						current_node = next_node
		root_node.print_nodes()

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

	def match_labels(self, root_node: Node):
		for child in root_node.children:
			depth = self.get_depth(child)

			#
			transitions = self.generate_all_strings(depth).pop()
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



