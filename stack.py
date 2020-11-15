class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return "Node [value: {}, next: {}]".format(self.value, self.next)

class Stack:
	def __init__(self):
		self.bottom = None
		self.size = 0

	def __str__(self):
		return "Stack [bottom: {}, size: {}]".format(self.bottom, self.size)

	def push(self, value):
		if not value:
			print("pass a valid value to push")
			return

		node = Node(value)
		node.next = self.bottom
		self.bottom = node
		self.size += 1

	def peek(self):
		return self.bottom.value

	def pop(self):
		node = self.bottom
		self.bottom = node.next
		self.size -= 1
		return node.value

	def isEmpty(self):
		if (self.size == 0):
			return True
		
		return False


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