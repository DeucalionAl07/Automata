from Node import Node
from Edge import Edge
class Graph:
	# Create graph representation for automata
	def __init__(self, val):
		# Constructor for Graph
		self.head = Node(val)
		self.nodes = []
		self.visited = []
		self.trans = []
		self.final_node = None
	def getHead(self):
		# Return head node
		return self.head
	def get_node(self, node, val):
		# Return node with particular value
		if node.val == val:
			return node
		else:
			for i in node.next:
				n = self.get_node(i, val)
				if n != None:
					return n
	def link(self, node1, node2, tok):
		# Link two nodes with an edge
		node1.next.append(node2)
		self.insert_edge(node1, node2, tok)
		return
	def insert_node(self, index_node, val, tok):
		# Inster node into the automata
		if val not in self.nodes:
			node = Node(val)
			self.nodes.append(val)
			index_node.next.append(node)
			self.insert_edge(index_node, index_node.next[-1], tok)
			return
		else:
			self.insert_edge(index_node, self.get_node(self.head, val), tok)
			return
	def insert_edge(self, from_, to_, tok):
		# Insert edge between two nodes
		edge = Edge(from_, to_, tok)
		from_.edges.append(edge)
		return
	def print_(self, node, tokens):
		# Display automata's transistion table
		string = "STATES"
		for i in tokens:
			string = string + "\t" + str(i)
		print string
		self.print1(node, tokens)
		self.visited = []
	def print1(self, node, tokens):
		# Prepare transition table of the automata
		string = [str(node.val)] + ["_"] * len(tokens)
		for i in node.edges:
			char = str(i.tok)
			for j in tokens:
				if char == str(j):
					if string[tokens.index(j)+1] != "_":
						string[tokens.index(j)+1] += "," + str(i.to_.val)	
					else:
						string[tokens.index(j)+1] = str(i.to_.val)
		val = string[0]
		for i in string[1:]:
			val = val + "\t" + str(i)
		print val
		for i in node.next:
			if i in self.visited:
				return
			self.visited.append(i)
			self.print1(i, tokens)		
	def final(self, node):
		# Return the final state of the automata
		self.final_(node)
		self.visited = []
		return self.final_node
	def final_(self, node):
		# Find the final node of the automata
		self.trans.append( node.val)
		if node.next == []:
			self.final_node = node
			return
		else:
			for i in node.next:
				if i in self.visited:
					continue
				self.visited.append(i)
				self.final_(i)
				return