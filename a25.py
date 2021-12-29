map = [list(x) for x in open("a25_input.txt").read().splitlines()]

height = len(map)
width = len(map[0])

def printmap():
    for row in map:
        print("".join(row))

def step():
    forward = []
    for y, row in enumerate(map):
        for x, c in enumerate(row):
            if c == '>':
                newx = (x+1) % width
                if map[y][newx] == '.':
                    forward.append((x,y,newx))
    for x,y, newx in forward:
        map[y][newx] = map[y][x]
        map[y][x] = '.'
    
    down = []
    for y, row in enumerate(map):
        for x, c in enumerate(row):
            if c == 'v':
                newy = (y+1) % height
                if map[newy][x] == '.':
                    down.append((x,y,newy))
    for x,y, newy in down:
        map[newy][x] = map[y][x]
        map[y][x] = '.'
    return len(forward) + len(down)

i=0
while True:
    i += 1
    moves = step()
    #print("After step", i)
    #printmap()
    #print("")
    if moves == 0:
        print("Part 1:", i)
        break