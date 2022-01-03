from utils import load
import collections

def extractParentAndChilds(line):
	if "no other" in line:
		parent = line.split(" bags contain no other bags")[0]
		children = []
	else:
		splitted = line.split(" bags contain ")
		parent = splitted[0]
		children = extractChildren(splitted[1])

	return (parent, children)


def extractChildren(line):
	splitted = line.split(", ")
	return [extractColor(item) for item in splitted]

def extractColor(item):
	if " bags" in item:
		numberColor = item.split(" bags")[0]
	elif " bag" in item:
		numberColor = item.split(" bag")[0]
	else:
		print("warning !!")

	number = int(numberColor.split(" ", 1)[0])
	color = numberColor.split(" ", 1)[1]
	return (number, color)

graph = {}

for line in load():
	(parent, children) = extractParentAndChilds(line)
	graph[parent] = set()
	for (number, color) in children:
		graph[parent].add((number, color))

# print(graph)

def containsShinyGold(parent, graph):
	if parent == "shiny gold":
		return True
	elif len(graph[parent]) == 0:
		return False

	return any([containsShinyGold(child, graph) for (number, child) in graph[parent]])


def countBags(parent, graph):
	return 1 + sum([number*countBags(child, graph) for (number, child) in graph[parent]])

## first problem
# count = 0
# for parent in graph:
# 	if parent != "shiny gold":
# 		containsSG = containsShinyGold(parent, graph)
# 		if containsSG:
# 			# print("for parent: ", parent)
# 			count += 1
# print(count)


## second problem
count = countBags("shiny gold", graph) - 1
print(count)


