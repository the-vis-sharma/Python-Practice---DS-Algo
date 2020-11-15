class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		return "[value: {}, next: {}]".format(self.value, self.next)

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __str__(self):
		return "[head: {}, tail: {}, size: {}]".format(self.head, self.tail, self.size)

	def append(self, value):
		if not value:
			print("pass a valid value to append")
			return

		node = Node(value)
		if self.size == 0:
			self.tail = node
			self.head = node
		else:
			self.tail.next = node
			self.tail = node
		self.size += 1

	def prepend(self, value):
		if not value:
			print("pass a valid value to prepend")
			return
		node = Node(value)
		node.next = self.head
		self.head = node

		if self.size == 0: 
			self.tail = node

		self.size += 1

	def insert(self, index, value):
		if not value:
			print("pass valid value to insert")
			return
		
		if index < 0 or index > self.size:
			print("index out of bound")
			return

		if index == 0 or index == self.size:
			self.append(value)
			return

		currentIndex = 0
		currentNode = self.head
		node = Node(value)
		while currentNode:
			if currentIndex == index - 1:
				node.next = currentNode.next
				currentNode.next = node
				self.size += 1
				break
			currentNode = currentNode.next
			currentIndex += 1

	def remove(self, index):
		if index < 0 or index > self.size:
			print("index out of bound")
			return

		if index == 0:
			self.head = None
			self.tail = None
			self.size = 0
			return

		currentIndex = 0
		currentNode = self.head
		while currentNode:
			if currentIndex == index - 1:
				currentNode.next = currentNode.next.next
				if index == self.size - 1:
					self.tail = currentNode
				self.size -= 1
				break
			
			currentNode = currentNode.next
			currentIndex += 1

	def reverse(self):
		prevNode = None
		nextNode = self.head
		currentNode = nextNode
		currentIndex = 0
		while currentNode:
			nextNode = currentNode.next
			currentNode.next = prevNode

			if currentIndex == 0:
				self.tail = currentNode
			elif currentIndex == self.size - 1:
				self.head = currentNode

			prevNode = currentNode
			currentNode = nextNode
			currentIndex += 1



myLinkedList = LinkedList()
print(myLinkedList)

myLinkedList.insert(0, 22)
myLinkedList.remove(0)
print(myLinkedList)
myLinkedList.insert(0, 25)
myLinkedList.reverse()
print(myLinkedList)

myLinkedList.prepend(2)
print(myLinkedList)

myLinkedList.append("")
myLinkedList.append(None)
myLinkedList.append([])

myLinkedList.append(5)
myLinkedList.append(10)
myLinkedList.append(16)
print(myLinkedList)

myLinkedList.insert(4, 1996)
print(myLinkedList)

myLinkedList.prepend("")
myLinkedList.prepend(None)
myLinkedList.prepend([])

myLinkedList.prepend(7)
print(myLinkedList)

myLinkedList.remove(6)
myLinkedList.remove(2)
print(myLinkedList)

myLinkedList.reverse()
print(myLinkedList)
