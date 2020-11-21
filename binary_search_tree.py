import json

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def __str__(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

class BST:
	def __init__(self):
		self.root = None

	def __str__(self):
		return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

	def insert(self, value):
		if not value:
			print("pass a valid value to insert method")
			return

		node = Node(value)
		if self.root == None:
			self.root = node
			return

		currentNode = self.root
		while (currentNode):
			if value < currentNode.value:
				if currentNode.left:
					currentNode = currentNode.left
				else:
					currentNode.left = node
					break
			elif value > currentNode.value:
				if currentNode.right:
					currentNode = currentNode.right
				else:
					currentNode.right = node
					break

	def find(self, value):
		if not value:
			print("pass a valid value to insert method")
			return

		if self.root == None:
			return False

		currentNode = self.root
		while (currentNode):
			if currentNode.value == value:
				return True
			elif currentNode.value < value:
				currentNode = currentNode.right
			else:
				currentNode = currentNode.left

		return False

	def setValueToParent(self, parentNode, node, value):
		if value < parentNode.value:
			parentNode.left = node
		else:
			parentNode.right = node


	def remove(self, value):
		if not value:
			print("pass a valid value to remove method")
			return

		if self.root is None:
			return

		currentNode = self.root
		parentNode = self.root
		while currentNode:
			if currentNode.value == value:
				if currentNode.left is not None and currentNode.right is not None:
					if currentNode.right.right is None and currentNode.right.left is None:
						currentNode.right.left = currentNode.left
						self.setValueToParent(parentNode, currentNode.right, currentNode.value)
						currentNode.right = None
					elif currentNode.right.left is not None:
						leftMostNode = currentNode.right.left
						pNode = currentNode.right
						while True:
							if leftMostNode.left is None:
								break
							pNode = leftMostNode
							leftMostNode = leftMostNode.left
						pNode.left = leftMostNode.right
						leftMostNode.left = currentNode.left
						leftMostNode.right = currentNode.right
						self.setValueToParent(parentNode, leftMostNode, currentNode.value)

				elif currentNode.left is not None:
					self.setValueToParent(parentNode, currentNode.left, currentNode.value)
				else:
					self.setValueToParent(parentNode, currentNode.right, currentNode.value)
				break
			elif currentNode.value < value:
				parentNode = currentNode
				currentNode = currentNode.right
			else:
				parentNode = currentNode
				currentNode = currentNode.left


		


myBST = BST()

print(myBST)

myBST.insert(9)
myBST.insert(4)
myBST.insert(20)
myBST.insert(1)
myBST.insert(6)
myBST.insert(15)
myBST.insert(170)
print(myBST)

print(myBST.find(60))

myBST.remove(6)
myBST.remove(4)
myBST.remove(20)
print("after deletion: ", myBST)

myBST.insert(180)
myBST.insert(178)
myBST.insert(185)
myBST.insert(175)
myBST.insert(176)
print(myBST)

myBST.remove(170)
print(myBST)
