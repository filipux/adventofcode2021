lines = open("a02_input.txt").read().splitlines()

# Part 1

depth = 0
pos = 0
for s in lines:
    command = s.split(" ")[0]
    value = int(s.split(" ")[1])
    if command == "forward":
        pos += value
    elif command == "up":
        depth -= value
    elif command == "down":
        depth += value

print(depth * pos)

# Part 2

depth = 0
pos = 0
aim = 0
for s in lines:
    command = s.split(" ")[0]
    value = int(s.split(" ")[1])
    if command == "forward":
        pos += value
        depth += aim * value
    elif command == "up":
        aim -= value
    elif command == "down":
        aim += value
print(depth * pos)