import re
from collections import namedtuple

# check if two cubes overlap
def overlap(c1, c2):
    if c1.x1 > c2.x2 or c1.x2 < c2.x1: return False
    if c1.y1 > c2.y2 or c1.y2 < c2.y1: return False
    if c1.z1 > c2.z2 or c1.z2 < c2.z1: return False
    return True

# check inner cube is completely inside outer cube
def inside(c, outer):
    if outer.x1 > c.x1 or outer.x2 < c.x2: return False
    if outer.y1 > c.y1 or outer.y2 < c.y2: return False
    if outer.z1 > c.z1 or outer.z2 < c.z2: return False
    return True

# volume of cube
def volume(c):
    return (c.x2-c.x1+1) * (c.y2-c.y1+1) * (c.z2-c.z1+1)

# return split segments on one axis
def segments(c1, c2, s1, s2):
    if s2 < c1 or s1 > c2:
        return [(c1,c2)]              # not overlapping
    elif s1 <= c1 and s2 < c2:
        return [(c1,s2), (s2+1, c2)]  # covers c1
    elif s1 > c1 and s2 >= c2:        
        return [(c1, s1-1), (s1,c2)]  # covers c2
    elif s1 <= c1 and s2 >= c2:
        return [(c1,c2)]              # covers both c1 and c2
    else: 
        return [(c1, s1-1),(s1,s2), (s2+1, c2)] #middle

# remove cube "s" from cube "c", returning list of subcubes
def remove(c, s):
    out = []

    xs = segments(c.x1, c.x2, s.x1, s.x2)
    ys = segments(c.y1, c.y2, s.y1, s.y2)
    zs = segments(c.z1, c.z2, s.z1, s.z2)
    for x1, x2 in xs:
        for y1, y2 in ys:
            for z1, z2 in zs:
                d=Cube('on', x1, x2, y1, y2, z1, z2)
                if not inside(d, s):
                    out.append(d)
    
    return out

# only return cubes inside safety area
def filtersafetyarea(cubes):
    return [c for c in cubes if all(abs(i) <= 50 for i in c[1:])]

# split and dice
def calculatevolume(cubes):
    res = []
    while len(cubes) > 0:
        s = cubes.pop(0)
        toremove = []
        toadd = []
        for c in res:
            if inside(c, s):
                toremove.append(c)
            elif overlap(c, s):
                toadd += remove(c,s)
                toremove.append(c)

        for r in toremove: res.remove(r)
        res += toadd
        if s.cmd: res.append(s)

    return sum([volume(x) for x in res])

# ----------

Cube = namedtuple('Cube', ['cmd','x1','x2','y1','y2','z1','z2'])
cubes = []

# read data
for r in open("a22_input.txt").read().splitlines():
    cmd, p = r.split(" ")
    p = Cube(cmd == 'on',*[int(x) for x in re.findall("[-\d]+", p)])
    cubes.append(p)

# do calculations
part1 = calculatevolume(filtersafetyarea(cubes))
part2 = calculatevolume(cubes)

print("Part1: ", part1)
print("Part2: ", part2)