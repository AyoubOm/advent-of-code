from utils import load
import re

instructions = load()

def toBinary(num):
	arr = [0]*36
	i = len(arr) - 1
	while num > 0:
		arr[i] = num % 2
		num = num // 2
		i -= 1
	return arr

def toDecimal(arr):
	num = 0
	for i, digit in enumerate(arr):
		num += digit << (35-i)
	return num

def decodeInstr(instr):
	if "mask" in instr:
		return ("mask", instr.split(" = ")[1])
	else:
		groups = re.search(r'mem\[(\d+)\] = (\d+)', instr)
		address = groups.group(1)
		value = groups.group(2)
		return ("mem", int(address), int(value))

## part 1
# mask = None
# memory = {}
# for instr in instructions:
# 	decoded = decodeInstr(instr)
# 	if decoded[0] == "mask":
# 		mask = decoded[1]
# 	else:
# 		(address, value) = (decoded[1], decoded[2])
# 		valueBin = toBinary(value)
# 		for i in range(36):
# 			if mask[i] == '0':
# 				valueBin[i] = 0
# 			elif mask[i] == '1':
# 				valueBin[i] = 1
# 		memory[address] = toDecimal(valueBin)


# print(sum(memory.values())) 

## part 2

def allAddresses(address, offset):
	i = offset
	while i < 36:
		if address[i] == 2:
			break
		i += 1

	if i >= 36:
		return [address]
	else: 
		first = address[:]
		first[i] = 0
		second = address[:]
		second[i] = 1
		return allAddresses(first, i + 1) + allAddresses(second, i + 1)



mask = None
memory = {}
for instr in instructions:
	decoded = decodeInstr(instr)
	if decoded[0] == "mask":
		mask = decoded[1]
	else:
		(address, value) = (decoded[1], decoded[2])
		addressBin = toBinary(address)
		for i in range(36):
			if mask[i] == '1':
				addressBin[i] = 1
			elif mask[i] == 'X':
				addressBin[i] = 2

		addresses = allAddresses(addressBin, 0)
		# print(addresses)
		for add in addresses:
			memory[toDecimal(add)] = value


print(sum(memory.values())) 





