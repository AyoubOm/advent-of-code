from utils import loadInput


l = [int(e) for e in loadInput("input.txt")]

for i in range(len(l)-2):
	for j in range(i+1, len(l)-1):
		for k in range(j+1, len(l)):
			if l[i]+l[j]+l[k] == 2020:
				print(l[i]*l[j]*l[k])


