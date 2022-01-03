from utils import load
import sys

lines = load()

arrivalEstimate = int(lines[0])
buses = [int(e) for e in lines[1].split(",") if e!='x']


minID = None
minWaitTime = sys.maxsize
for bus in buses:
	if arrivalEstimate % bus == 0:
		minID = bus
		minWaitTime = 0
	else:
		div = arrivalEstimate // bus
		waitTime = (bus*(div+1)) - arrivalEstimate
		if waitTime < minWaitTime:
			minWaitTime = waitTime
			minID = bus

# print(minID* minWaitTime)

k = 904
for i in range(100000000):
	k = 904*i

print(k)


