from typing import Optional, Type
from copy import copy, deepcopy

class Node:
	def __init__(self, data = 0, accepting = None):
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
			if(node.accepting == 'e'): 
				node.accepting = child.accepting
			
			self.children[self.children.index(child)] = node
			# self.children[int(child.value)] = node
		except:
			print("Child node not found")

	# TODO: Rewrite to use children position in array instead of value
	def transition(self, value):
		try:
			temp = self.children[int(value)]
			return temp
		except:
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
		return f"Data: {self.data}, acc: {self.accepting}"

	def __str__(self):
		return f"Data: {self.data}, acc: {self.accepting}, children: {self.children}"

	# Bad practice, just call str(object) instead, just for fun here
	def __add__(self, other):
		return str(self) + other

	def __radd__(self, other):
		return other + str(self)

	def __copy__(self):
		return type(self)(self.data)

	def __deepcopy__(self, memo):
		id_self = id(self)
		_copy = memo.get(id_self)
		if _copy is None:
			_copy = type(self)(
				deepcopy(self.data, memo),
				deepcopy(self.accepting, memo))
			memo[id_self] = _copy
			for child in self.children:
				_copy.children.append(deepcopy(child, memo))
			memo[id_self] = _copy
		return _copy