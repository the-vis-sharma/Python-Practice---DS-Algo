from node import Node

class Stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.size = 0

	def __str__(self):
		return "Stack [top: {}, bottom: {}, size: {}]".format(self.top, self.bottom, self.size)

	def push(self, value):
		if not value:
			print("pass a valid value to push")
			return

		node = Node(value)
		node.next = self.bottom
		self.bottom = node
		self.size += 1

		if (self.size == 1):
			self.top = self.bottom

	def peek(self):
		return self.top.value

	def pop(self):

		if self.isEmpty():
			print("StackUnderFlow error. There is nothing to pop in the stack, already empty.")
			return
			
		node = self.bottom
		self.bottom = node.next
		self.size -= 1

		if self.isEmpty():
			self.top = None
		return node.value

	def isEmpty(self):
		return self.size == 0


myStack = Stack()

print(myStack)

myStack.push("https://www.google.com/")
myStack.push("https://www.facebook.com/")
myStack.push("https://www.youtube.com/")
print(myStack)

print(myStack.peek())
print(myStack.peek())
print(myStack.pop())
print(myStack.pop())

print(myStack.isEmpty())
print(myStack.pop())
print(myStack.isEmpty())

print(myStack)