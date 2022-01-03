from utils import load

## part 1
# result = 0

# for instr in load():
# 	operations = []
# 	intermediates = []

# 	currentResult = 0
# 	currentOp = '+'

# 	for element in instr:
# 		if element == ' ':
# 			continue
# 		elif element in ['+', '*']:
# 			currentOp = element
# 		elif element == '(':
# 			intermediates.append(currentResult)
# 			operations.append(currentOp)
# 			currentResult = 0
# 			currentOp = '+'
# 		elif element == ')':
# 			lastResult = intermediates.pop()
# 			lastOp = operations.pop()
# 			if lastOp == '+':
# 				currentResult += lastResult
# 			else:
# 				currentResult *= lastResult
# 		else:
# 			if currentOp == '+':
# 				currentResult += int(element)
# 			else:
# 				currentResult *= int(element)

# 	result += currentResult


# print(result)

## part 2
result = 0

for instr in load():
	levels = []
	operations = []
	intermediates = []

	level = 0

	currentResult = 0
	currentOp = '+'

	for element in instr:
		if element == ' ':
			continue
		elif element == '+':
			currentOp = element
		elif element == '*':
			levels.append(level)
			intermediates.append(currentResult)
			operations.append('*')
			currentResult = 0
			currentOp = '+'
		elif element == '(':
			intermediates.append(currentResult)
			operations.append(currentOp)
			levels.append(level)
			level += 1
			currentResult = 0
			currentOp = '+'
		elif element == ')':
			level -= 1
			while levels and levels[-1] > level:
				lastResult = intermediates.pop()
				lastOp = operations.pop()
				levels.pop()
				if lastOp == '+':
					currentResult += lastResult
				else:
					currentResult *= lastResult
		else:
			if currentOp == '+':
				currentResult += int(element)

		# print(levels)
		# print(intermediates)
		# print(operations)
		# print("currentResult = ", currentResult)
		# print("--------")

	# print(intermediates)
	# print(operations, currentResult)

	while '+' in operations:
		if operations[-1] == '+':
			operations.pop()
			currentResult += intermediates[-1]
			intermediates.pop()
		else:
			index = operations.index('+')
			# print(intermediates[index], intermediates[index + 1])
			subRes = intermediates[index] + intermediates[index + 1]
			intermediates[index] = subRes
			intermediates.pop(index+1)
			operations.pop(index)

	for i, number in enumerate(intermediates):
		if operations[i] == '*':
			currentResult *= number

	result += currentResult


print(result)



def eval(expression):
	print(expression)
	minLevel = len(expression)

	currLevel = 0
	indexOp = -1
	op = None
	for i, c in enumerate(expression):
		if c == '(':
			currLevel += 1
		elif c == ')':
			currLevel -= 1

		elif (c == '*' and currLevel <= minLevel) or (currLevel < minLevel and c == '+'):
			op = c
			minLevel = currLevel
			indexOp = i

	if minLevel == len(expression): # int value
		return int(expression)

	else:
		if minLevel == 0:
			leftExp = expression[:indexOp-1]
			rightExp = expression[indexOp+2:]

		elif minLevel == 1:
			leftExp = expression[1:indexOp-1]
			rightExp = expression[indexOp+2:-1]

		else:
			print("bizarre => ", expression)
			exit()

		if op == '+':
			return eval(leftExp) + eval(rightExp)
		else:
			return eval(leftExp) * eval(rightExp)


result = 0
for expr in load():
	result += eval(expr)

print(result)



