with open("a14_input.txt") as file:
    poly = file.readline().strip()
    t = [tuple(x.split(" -> ")) for x in file.read().splitlines()[1:]]
    rules = {}
    for a,b in t:
        rules[a] = b

def calc(iterations):
    pairs = {}
    counts = {}
    for a, b in zip(poly, poly[1:]):
        pairs[a+b] = poly.count(a+b)

    for p in poly:
        counts[p] = poly.count(p)

    for i in range(iterations):
        newpairs = {}
        for a,b in pairs.items():
            if a in rules:
                b = rules[a]
                first = a[0]+b
                second = b+a[1]
                count = pairs[a] if a in pairs else 0
                newpairs[first] = newpairs[first] + count if first in newpairs else count            
                newpairs[second] = newpairs[second] + count if second in newpairs else count
                counts[b] = counts[b] + count if b in counts else count
            else:
                newpairs[a] = b
        pairs = newpairs
    return max(counts.values()) - min(counts.values())

print(calc(10))
print(calc(40))