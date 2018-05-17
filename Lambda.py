class Lambda:
	# Create lambda closure for a state
	def __init__(self, n):
		# Construct for Lambda
		self.node = n
		self.lambda_ = [n]
		self.visitedNodes = []
		self.makeLambda(self.node)
	def makeLambda(self, n):
		# Return the lambda closure
		if n in self.visitedNodes:
			return
		self.visitedNodes.append(n)
		for e in n.edges:
			if e.tok == '$':
				self.lambda_.append(e.to_)
				self.makeLambda(e.to_)
		return
	def printLambda(self):
		# Print the lambda closure
		l = [n.val for n in self.lambda_]
		print self.node.val, l