def findFirstRecurringChar(arr):
	if not arr:
		return
	mySet = set()
	for item in arr:
		if item in mySet:
			return item
		else:
			mySet.add(item)


print(findFirstRecurringChar([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(findFirstRecurringChar([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(findFirstRecurringChar([2, 3, 4, 5]))