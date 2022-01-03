from utils import load

def neighbors3(x, y, z):
	res = []
	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			for k in range(z-1, z+2):
				if (i, j, k) != (x, y, z):
					res.append((i, j, k))

	return res

def neighbors4(x, y, z, w):
	res = []
	for i in range(x-1, x+2):
		for j in range(y-1, y+2):
			for k in range(z-1, z+2):
				for l in range(w-1, w+2):
					if (i, j, k, l) != (x, y, z, w):
						res.append((i, j, k, l))

	return res


## part 1
actives = set()

matrix = [[e for e in line] for line in load()]

# for y, line in enumerate(load()):
# 	for x, cube in enumerate(line):
# 		if cube == '#':
# 			actives.add((x, y, 0))


# minX, maxX = 0, len(matrix[0])
# minY, maxY = 0, len(matrix)
# minZ, maxZ = 0, 0

# for _ in range(6):
# 	newActives = set()
# 	for x in range(minX - 1, maxX + 2):
# 		for y in range(minY - 1, maxY + 2):
# 			for z in range(minZ - 1, maxZ + 2):
# 				nbActives = 0
# 				neighbors = neighbors3(x, y, z)
# 				for n in neighbors:
# 					if n in actives:
# 						nbActives += 1

# 				if (x, y, z) in actives:
# 					if nbActives in [2, 3]:
# 						newActives.add((x, y, z))
# 				else:
# 					if nbActives == 3:
# 						newActives.add((x, y, z))

# 	minX, minY, minZ = minX - 1, minY - 1, minZ - 1 
# 	maxX, maxY, maxZ = maxX + 1, maxY + 1, maxZ + 1 
# 	actives = newActives
# 	print(newActives)

# print(len(actives))

for y, line in enumerate(load()):
	for x, cube in enumerate(line):
		if cube == '#':
			actives.add((x, y, 0, 0))


minX, maxX = 0, len(matrix[0])
minY, maxY = 0, len(matrix)
minZ, maxZ = 0, 0
minW, maxW = 0, 0

for _ in range(6):
	newActives = set()
	for x in range(minX - 1, maxX + 2):
		for y in range(minY - 1, maxY + 2):
			for z in range(minZ - 1, maxZ + 2):
				for w in range(minW - 1, maxW + 2):
					nbActives = 0
					neighbors = neighbors4(x, y, z, w)
					for n in neighbors:
						if n in actives:
							nbActives += 1

					if (x, y, z, w) in actives:
						if nbActives in [2, 3]:
							newActives.add((x, y, z, w))
					else:
						if nbActives == 3:
							newActives.add((x, y, z, w))

	minX, minY, minZ, minW = minX - 1, minY - 1, minZ - 1, minW - 1
	maxX, maxY, maxZ, maxW = maxX + 1, maxY + 1, maxZ + 1, maxW + 1
	actives = newActives

print(len(actives))







