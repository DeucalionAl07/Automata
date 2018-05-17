from Stack import Stack
class InfixToPostfix:
	# Convert RE to it's postfix form
	def __init__(self, exp):
		# Constructor for InfixToPostfix
		self.exp = exp
		self.stack = Stack()
		self.post_exp = ''	
	def doTrans(self):
		# Step by step conversion of the RE
		for i in list(self.exp):
			if i == '+':
				self.gotOper(i, 1)
			elif i == '.':
				self.gotOper(i, 2)
			elif i == '*':
				self.gotOper(i, 3)
			elif i == '(':
				self.stack.push(i)
			elif i == ')':
				self.gotParen()
			else:
				self.post_exp += i
			
		while self.stack.isEmpty() == False:
			self.post_exp += self.stack.pop()
			
		return self.post_exp
	def gotOper(self, opThis, prec1):
		# Dealing with operators
		while self.stack.isEmpty() == False:
			opTop = self.stack.pop()
			if opTop == '(':
				self.stack.push(opTop)
				break
			else:
				prec2 = 1
				if opTop == '.':
					prec2 = 2
				elif opTop == '*':
					prec2 = 3
				if prec2 < prec1:
					self.stack.push(opTop)
					break
				else:
					self.post_exp += opTop
		self.stack.push(opThis)		
	def gotParen(self):
		# Dealing with paranthesis
		while self.stack.isEmpty() == False:
			chx = self.stack.pop()
			if chx == '(':
				break
			else:
				self.post_exp += chx