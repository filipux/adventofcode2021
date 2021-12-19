dots = []
folds = []
for r in open("a13_test4.txt").read().splitlines():
    if ',' in r:
        dot = tuple(map(int, r.split(',')))
        dots.append(dot)
    elif '=' in r:
        axis, pos = r.split(" ")[-1].split('=')
        folds.append((axis, int(pos)))

def print_paper():
    w = 1+max([x for x,y in dots])
    h = 1+max([y for x,y in dots])
    c = [list("."*w) for r in range(h)]
    for x,y in dots:
        c[y][x] = "#"
    for r in c:
        print("".join(r))

for i,(axis, pos) in enumerate(folds):
    for id, (x,y) in enumerate(dots):
        if axis == 'x':
            if x > pos:
                dots[id] = (pos-(x-pos),y)
        if axis == 'y':
            if y > pos:
                dots[id] = (x, pos-(y-pos))
    if i == 0:
        print(len(set(dots)))

print_paper()
