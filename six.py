from utils import load


def countGroup(group):
	s = set()
	for person in group:
		for question in person:
			s.add(question)

	return len(s)


def countGroup2(group):
	s = set("abcdefghijklmnopqrstuvwxyz")
	for person in group:
		newS = set(s)
		for answer in s:
			if answer not in person:
				newS.remove(answer)

		s = newS

	return len(s) 


def countInput(nput):
	group = []
	_sum = 0
	for line in nput:
		if line:
			group.append(line)
		else:
			_sum += countGroup2(group)
			group = []

	_sum += countGroup2(group)
	return _sum



nput = load()
print(countInput(nput))
