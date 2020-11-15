# reverse a given string

def reverse(value):
	if value is None:
		return

	rev_value = []
	length = len(value)

	for i in reversed(range(length)):
		rev_value.append(value[i])

	return "".join(rev_value)


print(reverse('Hey! I\'m Vishnu'))