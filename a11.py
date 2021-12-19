import numpy as np

map = np.genfromtxt("a11_input.txt", dtype=int, delimiter=1)
height, width = map.shape

def neighbours(x,y):
    out = [(x-a,y-b) for b in range(-1,2) for a in range(-1,2)]
    return [(a,b) for a,b in out if a in range(width) and b in range(height) and (a,b) != (x,y)]

flashes = 0
sync = 9999999999
for step in range(999):
    map += 1
    while np.sum(map > 9):
        for y in range(height):
            for x in range(width):
                if map[y, x] > 9:
                    for a,b in neighbours(x,y):
                        if map[b, a] != -1:
                            map[b, a] += 1
                    map[y, x] = -1
                    if step < 100:
                        flashes += 1
    if np.sum(map < 0) == width*height:
        sync = min(sync, step+1)
    map[map < 0] = 0
    #print(map)
  
print("Flashes: ", flashes)
print("Sync step: ", sync)