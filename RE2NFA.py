from Stack import Stack
from Graph import Graph
class RE2NFA:
	# Convert RE to NFA
	def __init__(self, exp):
		# Constructor for RE2NFA
		self.stack = Stack()
		self.states = [-1]
		self.exp = exp
		self.OPER = ['+', '.', '*']
		self.CHAR = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		self.TOKENS = ['$']
		for i in list(exp):
			if i not in self.TOKENS and i in self.CHAR:
				self.TOKENS.append(i)
	def prim(self, tok):
		# Create new state for automata
		a = self.states[-1] + 1
		b = self.states[-1] + 2
		self.states.append(a)
		self.states.append(b)
		l = Graph(a)
		l.insert_node(l.head, b, tok)
		return l
	def doTrans(self):
		# Create the automata
		for tok in self.exp:
			if tok == '#':
				return self.stack.pop()
			elif tok in self.TOKENS:
				self.stack.push(self.prim(tok))
			elif tok in self.OPER:
				if tok == '.':
					op2 = self.stack.pop()
					op1 = self.stack.pop()
					fi = op1.final(op1.head)
					head = op2.head
					for i in head.edges:
						op1.link(fi, i.to_, i.tok)					
					self.stack.push(op1)
				if tok == '+':
					op2 = self.stack.pop()
					op1 = self.stack.pop()
					n = self.states[-1] + 1
					self.states.append(n)
					op = Graph(n)
					op.link(op.head, op1.head, '$')
					op.link(op.head, op2.head, '$')
					n = self.states[-1] + 1
					self.states.append(n)
					l = Graph(n)
					op.link(op.final(op.head.next[0]), l.head, '$')
					op.link(op.final(op.head.next[1]), l.head, '$')
					self.stack.push(op)
				if tok == '*':
					op = self.stack.pop()
					n = self.states[-1] + 1
					self.states.append(n)
					l1 = Graph(n)
					n = self.states[-1] + 1
					self.states.append(n)
					l2 = Graph(n)
					l1.link(l1.head, l2.head, '$')
					fi = op.final(op.head)
					op.link(fi, op.head, '$')
					op.link(fi, l2.head, '$')
					l1.link(l1.head, op.head, '$')
					self.stack.push(l1)
			else:
				print 'Enter a valid regular expression'
				return Graph(0)
