

def printimage(img):
    xmin = min([a for a,b in img])
    xmax = max([a for a,b in img])
    ymin = min([b for a,b in img])
    ymax = max([b for a,b in img])
    for y in range(ymin-1, ymax+2):
        line = ""
        for x in range(xmin-1, xmax+2):
            if (x, y) in img:
                line += "#"
            else:
                line += "."
        print(line)
        

def get3x3(map,x,y):
    str = ""
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if (i,j) in map:
                str += "1"
            else:
                str += "0"
    return int(str,2)


def enhance(map, pad):
    out = set()
    xmin = min([a-pad for a,b in map])
    xmax = max([a+pad for a,b in map])
    ymin = min([b-pad for a,b in map])
    ymax = max([b+pad for a,b in map])

    for y in range(ymin-1, ymax+2):
        for x in range(xmin-1, xmax+2):
            num = get3x3(map,x,y)
            res = algo[num]
            if res == "#":
                out.add((x,y))
            else:
                out.discard((x,y))
    return out

#-----------

# read data
algo, input= open("a20_input.txt").read().split("\n\n")
input = input.splitlines()

out = set()
for y, row in enumerate(input):
    for x, px in enumerate(row):
        if px == "#":
            out.add((x,y))

# iterate enhancement algorithm
for i in range(25):    
    out = enhance(out, pad=20)
    out = enhance(out, pad=-10)
    if i == 0:
        print("Part 1:", len(out))


print("Part 2:", len(out))
