from Lambda import Lambda
class NFA2DFA:
	# Convert NFA to DFA - Subset Construction
	def __init__(self, nfa, tokens):
		# Constructor for NFA2DFA
		self.NFA = nfa
		self.DFA = []
		self.TOKENS = tokens
		self.lambdas = []
		self.visitedNodes = []
	def getLambdas(self, n):
		# Get lambda closures of the states
		self.get_lambda(n)
		self.printLambdas()
		return
	def get_lambda(self, n):
		# Form the lambda closure for each state
		if n in self.visitedNodes:
			return
		self.visitedNodes.append(n)
		self.lambdas.append(Lambda(n))
		for next in n.next:
			self.get_lambda(next)
		return
	def printLambdas(self):
		# Print the lambda closures
		for l in self.lambdas:
			l.printLambda()
		return
	def makeDFA(self):

		return