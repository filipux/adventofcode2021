crabs = [int(x) for x in open("a07_input.txt").readline().split(",")]
print(min([sum([abs(c-i) for c in crabs]) for i in range(max(crabs))]))
print(min([sum([(abs(c-i) * (abs(c-i)+1))//2 for c in crabs]) for i in range(max(crabs))]))

