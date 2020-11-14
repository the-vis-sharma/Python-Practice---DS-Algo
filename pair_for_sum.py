# find the a pair whose sum is equal to given two number from two array.

# input: two array
# output: boolean

# we need less time 

from numpy import random
import time

# arr1 = [1, 2, 3, 4, 5]
# arr2 = [7, 8, 9, 5, 3, 0]

arr1 = random.randint(1000, size=(1000))
arr2 = random.randint(1000, size=(1500))

arr1.sort()
arr2.sort()

def isPairExistsBad(array1, array2, required_sum):
	startTime = time.time()
	for i in range(len(array1)):
		for j in range(len(array2)):
			if (array1[i] + array2[j] == required_sum):
				print("1st duration: ", (time.time() - startTime))
				return True
	print("1st duration: ", (time.time() - startTime))
	return False

print(isPairExistsBad(arr1, arr2, -17))

# O(n^2)

def isPairExistsBest(array1, array2, required_sum):
	startTime = time.time()
	temp = set(array2)
	for i in range(len(array1)):
		if ((required_sum - array1[i]) in temp):
			print("2nd duration: ", (time.time() - startTime))
			return True
	print("2nd duration: ", (time.time() - startTime))
	return False


print(isPairExistsBest(arr1, arr2, -17))

# O(n)


def isPairExistsGood(array1, array2, required_sum):
	startTime = time.time()
	i = 0
	j = len(array2) - 1
	while i < len(array1) and j >= 0:
		s = array1[i] + array2[j]
		if s == required_sum:
			print("3rd duration: ", (time.time() - startTime))
			return True
		elif s < required_sum:
			i += 1
		else:
			j -= 1
	print("3rd duration: ", (time.time() - startTime))
	return False

print(isPairExistsGood(arr1, arr2, -17))
# O(n)