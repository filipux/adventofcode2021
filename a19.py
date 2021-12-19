import math
import itertools as iter

class Point( object ):
    def __init__( self, x, y, z ):
        self.x, self.y, self.z = x, y, z
        self.hash = None
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y and self.z == p.z
    def distFrom( self, point ):
        return math.sqrt( (self.x-point.x)**2 + (self.y-point.y)**2 + (self.z-point.z)**2 )
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+","+ str(self.z)+")"
    __repr__ = __str__


def updatehashes(scanner):
    for b in scanner:
        dist = sorted([n.distFrom(b) for n in scanner])
        b.hash = round(13*dist[1] + 19*dist[2])

def rotate(beacons, pitch, roll, yaw):
    cosa = math.cos(yaw)
    sina = math.sin(yaw)
    cosb = math.cos(pitch)
    sinb = math.sin(pitch)
    cosc = math.cos(roll)
    sinc = math.sin(roll)
    
    Axx = cosa*cosb
    Axy = cosa*sinb*sinc - sina*cosc
    Axz = cosa*sinb*cosc + sina*sinc
    Ayx = sina*cosb
    Ayy = sina*sinb*sinc + cosa*cosc
    Ayz = sina*sinb*cosc - cosa*sinc
    Azx = -sinb
    Azy = cosb*sinc
    Azz = cosb*cosc
    out = []
    for p in beacons:
        q = Point(round(Axx*p.x+Axy*p.y+Axz*p.z), round(Ayx*p.x+Ayy*p.y+Ayz*p.z), round(Azx*p.x+Azy*p.y+Azz*p.z))
        q.hash = p.hash
        out.append(q)
    return out


def findbeaconwithhash(scanner, hash):
    for a in scanner:
        if a.hash == hash:
            return a
    return None

def matchingbeacons(b1,b2):
    tot = 0
    for b in b1:
        if b in b2:
            tot += 1
    return tot


def compare(b1,b2):
    if len(b1) != len(b2):
        print("NOT SAME LENGTH")
        return False
    for ib, b in enumerate(b1):
        if b1[ib] != b2[ib]:
            return False
    return True

def getcollisions(s1,s2):
    hash1 = set([c.hash for c in s1])
    hash2 = set([c.hash for c in s2])
    return hash1.intersection(hash2)

def findrotation(s1, s2):
    collisions = getcollisions(s1, s2)
    if len(collisions) == 0:
        #print("No collisions!")
        return (None, None)
    #print("Found collision", collisions)
    for hash in collisions:
        for r,s,t in iter.product([0, math.pi/2, math.pi, math.pi*1.5], repeat=3):
            rot = rotate(s2,r,s,t)

            p1 = findbeaconwithhash(s1, hash)
            p2 = findbeaconwithhash(rot, hash)

            # align rotated scanner so collision points match
            dx = (p2.x-p1.x)
            dy = (p2.y-p1.y)
            dz = (p2.z-p1.z)
            for ip, p in enumerate(rot):
                rot[ip].x = rot[ip].x - dx
                rot[ip].y = rot[ip].y - dy
                rot[ip].z = rot[ip].z - dz

            # after rotation and alignment, count matches (should be atleast 1)
            matchcount = matchingbeacons(s1, rot)
            #print(matchcount)
            if matchcount >= 12:
                #print("Found rotation for ", s1,s2)
                scannerpos = Point(-dx, -dy, -dz)
                return (scannerpos, rot)

    return (None, None)


#--------------

# Read data and compute neighborhood hashes
raw = [x.splitlines()[1:] for x in open("a19_input.txt").read().split("\n\n")]
scanners = [[Point(*map(int, a.split(","))) for a in r] for r in raw]
for b in scanners: updatehashes(b)

# iteratively find rotated scanners that align, then fix those
scannerpositions = [Point(0,0,0)]
fixed = [0]

while len(fixed) < len(scanners):
    for ia,a in enumerate(scanners):
        for ib,b in enumerate(scanners):
            if ia == ib: continue
            if ib in fixed: continue
            if ia not in fixed: continue
            (scannerpos, r) = findrotation(a,b)
            if r is not None: # we found a rotation that matches 12 beacons or more
                scanners[ib] = r
                scannerpositions.append(scannerpos)
                fixed.append(ib)
                print(ia,"<--",ib)
    print("linked scanners:", sorted(fixed))

# if we got this far we found a solution!!!!

if len(fixed) == len(scanners):
    # find number of unique beacons
    tot = []
    for b in scanners:
        for a in b:
            if not a in tot:
                tot.append(a)
    print("Part 1: ", len(tot))

    # find maximum manhattan distance of scanner pairs
    manhat = []
    for s in scannerpositions:
        for t in scannerpositions:
            manhat.append(abs(s.x-t.x)+abs(s.y-t.y)+abs(s.z-t.z))
    print("Part 2: ", max(manhat))