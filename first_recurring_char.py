def findFirstRecurringChar(arr):
	if not arr:
		return
	mySet = set()
	for item in arr:
		if item in mySet:
			return item
		else:
			mySet.add(item)

