from node import Node

class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.size = 0

	def __str__(self):
		return "Queue [first: {}, last: {}, size: {}]".format(self.first, self.last, self.size)

	def isEmpty(self):
		return self.size == 0

	def peek(self):
		if not self.isEmpty():
			return self.first.value

	def enqueue(self, value):
		if not value:
			print("pass a valid value to enqueue")
			return

		node = Node(value)

		if self.isEmpty():
			self.first = node
		else:
			self.last.next = node
		
		self.last = node
		self.size += 1

	def dequeue(self):
		if self.isEmpty():
			print("Queue is already empty. Nothing to dequeue")
			return

		node = self.first		
		self.first = node.next
		node.next = None
		self.size -= 1

		if self.isEmpty():
			self.last = None

		node.value


myQ = Queue()

print(myQ)

myQ.enqueue(2)
myQ.enqueue(5)
myQ.enqueue(10)
print(myQ)
		
myQ.dequeue()
print(myQ)
myQ.dequeue()
myQ.dequeue()
print(myQ)
	
