from utils import load
import collections

numbers = [int(e) for e in load()[0].split(",")]

spoken = collections.defaultdict(list)

for turn, n in enumerate(numbers):
	spoken[n] = [turn+1]

turn = len(numbers)+1

lastSpoken = numbers[-1]
while turn <= 30000000:
	times = spoken[lastSpoken]
	if len(times) >= 2:
		lastSpoken = times[-1] - times[-2]
	else:
		lastSpoken = 0
	spoken[lastSpoken].append(turn)

	turn += 1

print(lastSpoken)
