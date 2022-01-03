from utils import load


ranges = []

takeTicket = False
myTicket = None
tickets = []

def readTicket(ticket):
	return [int(e) for e in ticket.split(',')]

for line in load():
	if "or" in line:
		ranges.append((line.split(": ")[0], [int(e) for r in line.split(": ")[1].split(" or ") for e in r.split("-")]))
	elif "your" in line:
		takeTicket = True
	elif takeTicket:
		myTicket = readTicket(line)
		takeTicket = False
	elif ',' in line:
		tickets.append(readTicket(line))

tickets.reverse()

valids = [True for _ in range(len(tickets))]
sumInvalids = 0
for i, ticket in enumerate(tickets):
	for value in ticket:
		found = False
		for r in ranges:
			r = r[1]
			if (value >= r[0] and value <= r[1]) or (value >= r[2] and value <= r[3]):
				found = True
				break
		if not found: 
			sumInvalids += value
			valids[i]= False




def backtrack(column, mappings):
	print(mappings)
	if column >= len(ranges):
		return True
	for rangeCouple in ranges:
		if rangeCouple[0] not in mappings:
			found = True
			r = rangeCouple[1]
			for i, ticket in enumerate(tickets):
				if valids[i]:
					value = ticket[column]
					if not ((value >= r[0] and value <= r[1]) or (value >= r[2] and value <= r[3])):
						found = False
						break

			if found:
				mappings[rangeCouple[0]] = column
				if backtrack(column+1, mappings):
					return True
				else:
					mappings.pop(rangeCouple[0])

	return False

mappings = {}
backtrack(0, mappings)

result = 1
for k, v in mappings.items():
	if "departure" in k:
		result *= myTicket[v]

print(result)



			





