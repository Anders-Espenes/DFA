from typing import Optional, Type


class Node:
	def __init__(self, value, data, accepting):
		self.value = value
		self.data = data
		self.accepting: bool = accepting
		self.children: list[Node] = []

	def setChild(self, child):
		self.children.append(child)

	def removeChild(self, child):
		self.children.remove(child)

	def transition(self, value):
		for child in self.children:
			if child.value == value:
				return child
		else:
			return None

	def print_nodes(self):
		"""Prints node and all child nodes in depth first order"""
		print(self)
		for child in self.children:
			child.print_nodes()

	def __repr__(self):
		return f"Data: {self.data}, acc: {self.accepting}"
