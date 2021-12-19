import itertools as iter

lines = open("a08_input.txt").read().splitlines()
input = [r.split(" | ")[0].split(" ") for r in lines]
output = [r.split(" | ")[1].split(" ") for r in lines]

def decode(seg, key):
    dec = set()
    for v in seg:
        dec.add(key["abcdefg".index(v)])
    return dec

segs1 = [set(x) for x in ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]]
segs2 = [set(x) for x in ["deagbc", "ab", "dafgc", "dafbc", "eafb", "defbc", "defgbc", "dab", "deafgbc", "deafbc"]]
keys = list(iter.permutations("abcdefg", 7))

# ----- Part 1 -----


digits = [0 for x in range(10)]
for ir, row in enumerate(input):
    for key in keys:
        decodedRow = [decode(word, key) for word in row]
        matches = sum([(d in segs1) for d in decodedRow])
        if matches == 10:
            for word in output[ir]:
                decodedWord = decode(word, key)
                digit = segs1.index(decodedWord)
                digits[digit] += 1
            break

print("PART 1:", digits[1] + digits[4] + digits[7] + digits[8])

# ----- Part 2 -----

digitSum = 0
for ir, row in enumerate(input):
    for key in keys:
        decodedRow = [decode(word, key) for word in row]
        matches = sum([(d in segs2) for d in decodedRow])
        if matches == 10:
            num = ""
            for word in output[ir]:
                decodedWord = decode(word, key)
                digit = segs2.index(decodedWord)
                num += str(digit)
            digitSum += int(num)
            break

print("PART 2:", digitSum)
