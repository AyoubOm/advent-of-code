from utils import load


## first part
# size = 25

# numbers = [int(e) for e in load()]
# N = len(numbers)

# for current in range(size, N):
# 	flag = False
# 	# print(current)
# 	for j in range(current - size, current - 1):
# 		for k in range(j+1, current):
# 			if numbers[j] + numbers[k] == numbers[current]:
# 				# print(numbers[current], " = ", numbers[j], " + ", numbers[k])
# 				flag = True
# 				break
# 		if flag:
# 			break

# 	if not flag:
# 		print(numbers[current])
# 		break


## second part
size = 25

numbers = [int(e) for e in load()]
N = len(numbers)

def findInvalid():
	for current in range(size, N):
		flag = False
		# print(current)
		for j in range(current - size, current - 1):
			for k in range(j+1, current):
				if numbers[j] + numbers[k] == numbers[current]:
					# print(numbers[current], " = ", numbers[j], " + ", numbers[k])
					flag = True
					break
			if flag:
				break

		if not flag:
			return current
			break

invalid = findInvalid()


def indexes():
	for i in range(invalid-1):
		for j in range(i+1, invalid):
			if sum(numbers[i:j+1]) == numbers[invalid]:
				return (i, j)


(i, j) = indexes()
subset = numbers[i:j+1]
mini, maxi = min(subset), max(subset)
print(mini+maxi)
