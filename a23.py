
import heapq
from collections import namedtuple


Pod = namedtuple('Pod', ['type', 'x', 'y', 'state', 'points'])


def solve(map):
    pods = []

    def copy(map):
        return [[i for i in row] for row in map]
    
    emptymap = copy(map)

    # read
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell in ['A', 'B', 'C', 'D']:
                pods.append(Pod(cell, x, y, "start", 0))
                emptymap[y][x] = "."

    def updatemap(pods):
        b = copy(emptymap)
        for p in pods: b[p.y][p.x] = p.type
        return b

    def printmap(pods):
        b = copy(emptymap)
        for p in pods: b[p.y][p.x] = p.type
        for r in b: print("".join(r))
            
    def movepoints(org, pod):
        dist = abs(org.x-pod.x)+abs(org.y-pod.y)
        points = dist * {'A':1, 'B':10, 'C':100, 'D':1000}[org.type]
        return points

    def cango(pod, map):
        out = []
        if pod.state == "start":
            if not all([map[y][pod.x] == "." for y in range(pod.y-1, 1, -1)]):
                return []

            for x in range(pod.x, 13): # search right
                if map[1][x] != ".": break
                if map[2][x] == "#":
                    out.append(Pod(pod.type, x, 1, "hall", pod.points))
            for x in range(pod.x-1,0,-1): #search left
                if map[1][x] != ".": break
                if map[2][x] == "#":
                    out.append(Pod(pod.type, x, 1, "hall", pod.points))
        
        elif pod.state == "hall":
            tx = "###A#B#C#D###".index(pod.type)
            dx = +1 if tx > pod.x else -1
            if all([map[1][x] == "." for x in range(pod.x+dx, tx, dx)]): # hela vägen fram i x led okej
                r = [map[y][tx] for y in range(2, len(map)-1)]
                if all([c in {".", pod.type} for c in r]):
                    y = 1 + r.count(".")
                    out.append(Pod(pod.type, tx, y, "done", pod.points))    

        out = [Pod(p.type, p.x, p.y, p.state, pod.points + movepoints(pod, p)) for p in out]
        return out
                

    # detta är sån skitlösning att jag mår illa

    best = 9999999999
    pq = [(0, pods)]
    history = set()
    while len(pq) > 0:
        _, pods = heapq.heappop(pq)
        tot = sum([p.points for p in pods])
        if tot > best: continue
        if tuple(pods) in history: continue

        history.add(tuple(pods))

        if all([p.state == "done" for p in pods]):
            if tot < best:
                best = tot
        else:
            mapppp = updatemap(pods)
            for p in pods:
                for newp in cango(p, mapppp):
                    newpods = [pod if pod != p else newp for pod in pods]
                    tot1 = -sum([p.state == "done" for p in newpods])
                    tot3 = abs(newp.x-p.x)+abs(newp.y-p.y)
                    heapq.heappush(pq, (tot1+tot3, newpods))

    print("Completed: ", best)




map1 = [list(r) for r in open("a23_input.txt").read().splitlines()]    
map2 = [list(r) for r in open("a23_input.txt").read().splitlines()]
map2.insert(3, list("  #D#C#B#A#  "))
map2.insert(4, list("  #D#B#A#C#  "))
solve(map1)
solve(map2)
