def sum(*l):
	sum = 0
	print(l)
	for num in l:
		sum += num

	return sum

print(sum([1, 2, 3]))