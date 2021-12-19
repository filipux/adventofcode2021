import numpy as np

map = np.genfromtxt("a09_input.txt", dtype=int, delimiter=1)
map = np.pad(map, 1, 'maximum')

risks = 0
lowpoints = []
for y in range(1,len(map)-1):
    for x in range(1,len(map[y])-1):
        value = map[y,x]
        neighbours = [map[d[1]+y, d[0]+x] for d in [(-1,0), (+1,0), (0,-1), (0,+1)]]
        if sum(neighbours <= value) == 0:
            risks += value + 1
            lowpoints.append((x,y))

print(risks)

def basin(lowpoint):
    seen = []
    q = [lowpoint]
    while len(q) > 0:
        p = q.pop()
        seen.append(p)
        neighbours = [(d[0]+p[0], d[1]+p[1]) for d in [(-1,0), (+1,0), (0,-1), (0,+1)]]
        neighbours = [n for n in neighbours if n not in seen and n not in q]
        neighbours = [n for n in neighbours if map[n[1], n[0]] > map[p[1], p[0]]]
        neighbours = [n for n in neighbours if map[n[1], n[0]] < 9]
        q += neighbours
    return seen

basins = [len(basin(p)) for p in lowpoints]
print(np.prod(sorted(basins)[-3:]))