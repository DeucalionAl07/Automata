class Node:
	# Create Node for the automata
	def __init__(self, val=None):
		# Constructor for Node
		self.val = val
		self.next = []
		self.edges = []