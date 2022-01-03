from utils import load
import collections

ratings = [int(e) for e in load()]

## part 1

# differences = collections.defaultdict(int)
# ratings.sort()

# current = 0
# for rating in ratings:
# 	differences[rating-current] += 1
# 	current = rating

# differences[3] += 1

# mult = differences[1]*differences[3]

# print(mult)

## part 2

ratings = [int(e) for e in load()]
s = set(ratings)
maxi = max(ratings)

# dico = {}
from functools import lru_cache

@lru_cache(maxsize = 100)
def recurse(rating):
	# if rating in dico:
	# 	return dico[rating]
	if rating == maxi:
		return 1
	elif rating != 0 and rating not in s:
		return 0
	else:
		value = recurse(rating+1)+recurse(rating+2)+recurse(rating+3)
		# dico[rating] = value
		return value

print(recurse(0))
