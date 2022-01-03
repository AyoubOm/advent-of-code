from utils import load

nonTerminals = {}
terminals = {}

messages = []

isRule = True

for rule in load():
	if not rule:
		isRule = False

	elif isRule:
		splitted = rule.split(": ")
		nb = splitted[0]
		if '"' not in splitted[1]:
			if '|' in splitted[1]:
				splitted = splitted[1].split(' | ')
			else:
				splitted = [splitted[1]]

			for i in range(len(splitted)):
				splitted[i] = splitted[i].split(' ')

			nonTerminals[nb] = splitted

		elif splitted[1] == '"a"':
			terminals[nb] = "a"

		elif splitted[1] == '"b"':
			terminals[nb] = "b"

	else:
		messages.append(rule)


# print(nonTerminals)

# def isValid(message):
# 	def helper(message, current, rule):
# 		if current >= len(message):
# 			return -1
# 		if rule in terminals:
# 			if message[current] != terminals[rule]:
# 				return -1
# 			else:
# 				return current + 1
# 		else:
# 			match = False
# 			for sequence in nonTerminals[rule]: 
# 				for rule in sequence:
# 					current = helper(message, current, rule)
# 					if current == -1



def possibleMatches(rule):
	if rule in terminals:
		return [terminals[rule]]
	else:
		matches = []
		for sequence in nonTerminals[rule]:
			prefixes = [""]
			for rule in sequence:
				newPrefixes = []
				for match in possibleMatches(rule):
					for prefix in prefixes:
						newPrefixes.append(prefix+match)
				prefixes = newPrefixes
			matches += prefixes
		return matches



matches42 = set(possibleMatches('42'))
size = len(possibleMatches('42')[0])
print("size = ", size)
matches31 = set(possibleMatches('31'))


print(matches42)
print(matches31.difference(matches42))
# 0: 8 11 = (42_k 31_n) k > n


def isMatch(msg, size):
	print("message = ", msg)
	if len(msg) % size or len(msg) == size*2:
		return False

	firstHalf = len(msg)//2
	for i in range(0, firstHalf, size):
		if msg[i:i+size] not in matches42:
			return False

	begin31 = False
	for i in range(firstHalf+size, len(msg)-size, size):
		if begin31:
			if msg[i: i+size] not in matches31:
				return False
		elif msg[i:i+size] not in matches42:
			if msg[i: i+size] not in matches31:
				return False
			begin31 = True

	print("index = ", len(msg)-size)
	if msg[len(msg)-size:] not in matches31:
		return False

	return True


print(sum([isMatch(msg, size) for msg in messages]))

