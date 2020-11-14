def mergeArray(arr1, arr2):
	mergedArray = []
	if arr1 is None or arr2 is None:
		return mergedArray
	elif len(arr1) <= 0:
		return arr2
	elif len(arr2) <= 0:
		return arr1

	i = 0
	j = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j]:
			mergedArray.append(arr1[i])
			i += 1
		else:
			mergedArray.append(arr2[j])
			j += 1

	while i < len(arr1):
		mergedArray.append(arr1[i])
		i += 1

	while j < len(arr2):
		mergedArray.append(arr2[j])
		j += 1

	return mergedArray

# O(n)