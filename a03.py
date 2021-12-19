lines = open("a03_input.txt").read().splitlines()

# Part 1

gamma = ""
epsilon = ""

for i in range(len(lines[0])):
    col = [x[i] for x in lines]
    if col.count("1") > col.count("0"):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
print("Part 1:", int(gamma, base=2) * int(epsilon, base=2))

# Part 2

oxy = lines

for i in range(len(lines[0])):
    col = [x[i] for x in oxy]
    if col.count("1") >= col.count("0"):
        oxy = [x for x in oxy if x[i] == "1"]
    else:
        oxy = [x for x in oxy if x[i] == "0"]


scrub = lines

for i in range(len(lines[0])):
    col = [x[i] for x in scrub]
    if len(col) == 1: break
    if col.count("0") <= col.count("1"):
        scrub = [x for x in scrub if x[i] == "0"]
    else:
        scrub = [x for x in scrub if x[i] == "1"]

print(int(oxy[0], base=2) * int(scrub[0], base=2))
