from utils import load


def decodeSeat(seat):
	lo = 0
	hi = 127
	for i in range(7):
		middle = (lo+hi)//2
		if seat[i] == 'F':
			hi = middle
		else:
			lo = middle + 1

	row = lo

	lo = 0
	hi = 7
	for j in range(7, len(seat)):
		middle = (lo + hi) // 2
		if seat[j] == 'L':
			hi = middle
		else:
			lo = middle + 1

	col = lo
	return (row, col)

def seatID(row, col):
	return row*8 + col


seats = load()

maxSeatID = 0
minSeatID = 127 * 8 + 7
seatIDs = set()

for seat in seats:
	(row, col) = decodeSeat(seat)
	seat_id = seatID(row, col)
	maxSeatID = max(maxSeatID, seat_id)
	minSeatID = min(minSeatID, seat_id)
	seatIDs.add(seat_id)


print(minSeatID, maxSeatID)

for s in range(128 * 8):
	if (s not in seatIDs) and s > minSeatID and s < maxSeatID:
		print(s)




