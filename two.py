from utils import loadInput
import collections

def parse(inputList):
	result = []
	for element in inputList:
		(composed, password) = element.split(": ")[0], element.split(": ")[1]
		composed = composed.split(" ")
		(minOcc, maxOcc, character) = (int(composed[0].split("-")[0]), int(composed[0].split("-")[1]), composed[1])
		result.append((minOcc, maxOcc, character, password))

	return result

parsedData = parse(loadInput("input.txt"))

def firstPolicy():
	result = 0
	for (minOcc, maxOcc, character, password) in parsedData:
		numberOcc = password.count(character)
		if numberOcc >= minOcc and numberOcc <= maxOcc:
			result += 1

	print("result: ", result)

def secondPolicy():
	result = 0
	for (firstPos, secondPos, character, password) in parsedData:
		inFirst = password[firstPos-1]==character
		inSecond = password[secondPos-1]==character
		if (inFirst and (not inSecond)) or (inSecond and (not inFirst)):
			result += 1

	print("result: ", result)

secondPolicy()

