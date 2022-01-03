from utils import load

digits = "0123456789"


def validateHcl(hcl):
	tok = hcl[0] == '#' and all([(e in digits) or (e in "abcdef") for e in hcl[1:]]) and len(hcl) == 7
	# print(tok)
	return tok

def validateEcl(ecl):
	l = ["amb", "blu", "brn","gry" ,"grn" ,"hzl", "oth"]
	return ecl in l

def validatePid(pid):
	return len(pid)==9 and all([e in digits for e in pid])


def validateHgt(hgt):
	cond = False
	if "cm" in hgt:
		tok = int(hgt.split("cm")[0])
		cond = tok >= 150 and tok <= 193
	elif "in" in hgt:
		tok = int(hgt.split("in")[0])
		cond = tok >= 59 and tok <= 76
	return cond


rows = load()

keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

current = {}

result = 0

for row in rows:
	if row == "":
		diff = list(set(keys) - set(current.keys()))
		print(current)
		# print(diff)
		byr = current.get("byr", 0)
		iyr = current.get("iyr", 0)
		eyr = current.get("eyr", 0)
		hgt = current.get("hgt", "")
		pid = current.get("pid", "0")
		ecl = current.get("ecl", "")
		hcl = current.get("hcl", "0")
		# print(byr, iyr, eyr, hgt, pid, ecl, hcl)
		if ((not diff) or (len(diff) == 1 and diff[0] == "cid")) and int(byr) >= 1920 and int(byr) <= 2002 and int(iyr) >= 2010 and int(iyr) <= 2020 and int(eyr) >= 2020 and int(eyr) <= 2030 and validateHgt(hgt) and validateHcl(hcl) and validateEcl(ecl) and validatePid(pid):
			result += 1
		current = {}

	else:
		splitted = row.split(" ")
		dictKeys = [e.split(":")[0] for e in splitted]
		dictValues = [e.split(":")[1] for e in splitted]
		dico = dict(zip(dictKeys, dictValues))
		current = dict(list(current.items()) + list(dico.items()))

diff = set(keys) - set(current.keys())
byr = current.get("byr", 0)
iyr = current.get("iyr", 0)
eyr = current.get("eyr", 0)
hgt = current.get("hgt", "")
pid = current.get("pid", "0")
ecl = current.get("ecl", "")
hcl = current.get("hcl", "0")
if ((not diff) or (len(diff) == 1 and diff[0] == "cid")) and int(byr) >= 1920 and int(byr) <= 2002 and int(iyr) >= 2010 and int(iyr) <= 2020 and int(eyr) >= 2020 and int(iyr) <= 2030 and validateHgt(hgt) and validateHcl(hcl) and validateEcl(ecl) and validatePid(pid):
	result += 1

print(result)
