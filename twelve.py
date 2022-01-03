from utils import load

instructions = load()

## part1
# east = 0
# north = 0

# direction = [1, 0]

# def decode(instr):
# 	return (instr[0], int(instr[1:]))

# for instr in instructions:
# 	(instr, number) = decode(instr)
# 	if instr == 'N':
# 		north += number
# 	elif instr == 'S':
# 		north -= number
# 	elif instr == 'E':
# 		east += number
# 	elif instr == 'W':
# 		east -= number
# 	elif instr == 'F':
# 		east += direction[0]*number
# 		north += direction[1]*number
# 	else:
# 		number = number % 360
# 		for _ in range(number//90):
# 			if instr == 'L':
# 				direction[0], direction[1] = -direction[1], direction[0]
# 			else:
# 				direction[0], direction[1] = direction[1], -direction[0]

# 	# print(instr+str(number), east, north)


# print(abs(east)+abs(north))


## part 2
east = 0
north = 0

waypoint = [10, 1]

def decode(instr):
	return (instr[0], int(instr[1:]))

for instr in instructions:
	(instr, number) = decode(instr)
	if instr == 'N':
		waypoint[1] += number
	elif instr == 'S':
		waypoint[1] -= number
	elif instr == 'E':
		waypoint[0] += number
	elif instr == 'W':
		waypoint[0] -= number
	elif instr == 'F':
		east += waypoint[0]*number
		north += waypoint[1]*number
	else:
		number = number % 360
		for _ in range(number//90):
			if instr == 'L':
				waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
			else:
				waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]

	# print(instr+str(number), east, north)


print(abs(east)+abs(north))


