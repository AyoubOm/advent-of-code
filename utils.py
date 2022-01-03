def loadInput(filename):
	res = []
	with open(filename, 'r') as f:
		for l in f.read().splitlines():
			res.append(l)
	return res

def load():
	return loadInput("input.txt")
