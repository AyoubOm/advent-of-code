from utils import load



def computeTrees(rows, right, down):
	rowSize = len(rows[0])-1
	result = 0
	# print("row size : ", rowSize)
	for i, row in enumerate(rows):
		if (i % down) == 0:
			print(i)
			if row[(right*(i//down))%rowSize] == '#':
				result += 1

	return result


rows = load()
# print(computeTrees(rows, 3, 1))

l = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
res = 1
for (right, down) in l:
	# print(right, down)
	res *= computeTrees(rows, right, down)
print(res)
	