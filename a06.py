fish = [int(x) for x in open("a06_input.txt").readline().split(",")]

# ----- Part 1 -----

def slowStep(fish, days):
    for i in range(days):
        fish += [9 for x in range(fish.count(0))] 
        fish = [6 if x == 0 else (x-1) for x in fish]
    return len(fish)

print("Step 1:", slowStep(fish, 80))

# ----- Part 2 -----

def fastStep(fish, days):
    tot = len(fish)
    counts = [fish.count(i) for i in range(9)]

    for i in range(days):
        zeros = counts[0]
        counts[0] = counts[1]
        counts[1] = counts[2]
        counts[2] = counts[3]
        counts[3] = counts[4]
        counts[4] = counts[5]
        counts[5] = counts[6]
        counts[6] = counts[7] + zeros
        counts[7] = counts[8]
        counts[8] = zeros
        tot += zeros
    return tot

print("Step 2:", fastStep(fish, 256))