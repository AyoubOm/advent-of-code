from utils import load

## first part
# acc = 0

# instructions = load()
# executed = set()

# i = 0
# while i not in executed:
# 	instruction = instructions[i]
# 	splitted = instruction.split(" ") 
# 	opcode = splitted[0]
# 	argument = int(splitted[1])

# 	if opcode == "acc":
# 		acc += argument
# 	elif opcode == "jmp":
# 		i += argument
# 		continue

# 	executed.add(i)

# 	i += 1

# print(acc)


## second part
instructions = load()

def split(instruction):
	splitted = instruction.split(" ") 
	opcode = splitted[0]
	argument = int(splitted[1])
	return (opcode, argument)

def loop():
	acc = 0
	executed = set()
	i = 0
	while i not in executed and i < len(instructions):
		# print(i)
		instruction = instructions[i]
		(opcode, argument) = split(instruction)

		executed.add(i)

		if opcode == "acc":
			acc += argument
		elif opcode == "jmp":
			i += argument
			continue


		i += 1
	
	return (i >= len(instructions), acc)


N = len(instructions)
for i in range(N):
	# print("trying ", i, "th instruction")
	instruction = instructions[i]
	(opcode, argument) = split(instruction)
	if opcode == "jmp":
		instructions[i] = "nop " + str(argument)
		(noCycle, acc) = loop()
		if noCycle:
			print(acc)
			exit()
		instructions[i] = "jmp " + str(argument)

	elif opcode == "nop":
		instructions[i] = "jmp " + str(argument)
		(noCycle, acc) = loop()
		if noCycle:
			print(acc)
			exit()
		instructions[i] = "nop " + str(argument)


