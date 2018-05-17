class Stack:
	# Stack item for expression conversion
	def __init__(self):
		# Constructor for Stack
		self.stack = []
		self.top = -1
	def push(self, val):
		# Push item into stack
		self.top += 1
		self.stack.append(val)
	def pop(self):
		# Return item from stack
		if self.top < 0:
			raise Exception('Stack Empty => Enter a correct expression')
		else:
			self.top -= 1
			return self.stack.pop()
	def isEmpty(self):
		# Check if stack is empty
		if self.top == -1:
			return True
		return False