class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None

	def __str__(self):
		return "[key: {}, value: {}, next: {}]".format(self.key, self.value, self.next)

	def __repr__(self):
		return self.__str__()

class MyHashMap:
	def __init__(self, size):
		self.size = size
		self.data = [None] * size

	def keyToHash(self, key):
		hash = 0
		keyLen = len(key)
		for i in range(keyLen):
			hash = (hash + ord(key[i]) * keyLen) % self.size

		return hash

	def insert(self, key, value):
		hash = self.keyToHash(key)
		node = Node(key, value)
		if self.data[hash]:
			linkedList = self.data[hash]
			found = False
			while linkedList:
				if linkedList.key == key:
					linkedList.value = value
					found = True
					break
				linkedList = linkedList.next
			if not found:
				self.data[hash].next = node
		else:
			self.data[hash] = node

	def get(self, key):
		value = None
		hash = self.keyToHash(key)
		node = self.data[hash]
		while node:
			if node.key == key:
				value = node.value
				break
			node = node.next

		return value

	def keys(self):
		allKeys = []
		for i in range(self.size):
			node = self.data[i]
			while node:
				allKeys.append(node.key)
				node = node.next

		return allKeys
