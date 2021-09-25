from typing import Optional, Type

class Node:
	def __init__(self, value, data, accepting):
		self.value = value							# 
		self.data = data							#
		self.accepting: bool = accepting 			# Label, true DFA allows ending of input strings here
		self.children: list[Node] = [] 				# Child nodes left to right

	def addChild(self, child):
		self.children.append(child)

	def removeChild(self, child):
		self.children.remove(child)
	
	# Set a child node to given node
	def setChild(self, child, node):
		"""Changes childs reference to given node"""
		try:
			# Set empty node
			if(node.data == 'e'): 
				node.value = child.value
			
			# self.children[self.children.index(child)] = node
			self.children[int(child.value)] = node
		except:
			print("Child node not found")

	def transition(self, value):
		for child in self.children:
			if child.value == value:
				return child
		else:
			return None
	
	def next(self, index):
		return self.children[int(index)]


	def getChild(self, node):
		""" Find a given node amongst the children """
		for child in self.children:
			if node == child and child != self:
				return child
		return None

	def destroy(self):
		for child in self.children: # Remove children
			child.destroy()
		del self

	def print_nodes(self, unique):
		"""Prints node and all child nodes in depth first order"""
		unique.append(self)
		print(self)
		for child in self.children:
			if child not in unique:  # To prevent calling on a reference to self
				child.print_nodes(unique)


	def __repr__(self):
		'''This method returns an offical string representation of an object
		And is supposed to be used to convert the entire object to a string format
		TLDR: Not meant for printing use __str__ instead'''
		return f"Data: {self.data}, acc: {self.accepting}, value: {self.value}"

	def __str__(self):
		return f"Data: {self.data}, acc: {self.accepting}, children: {self.children}"

	# Bad practice, just call str(object) instead, just for fun here
	def __add__(self, other):
		return str(self) + other

	def __radd__(self, other):
		return other + str(self)
