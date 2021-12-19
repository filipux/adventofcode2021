import numpy as np
from collections import namedtuple

Line = namedtuple('Line', ['x1', 'y1', 'x2', 'y2'])
lines = [Line(*map(int, x.replace(" -> ", ",").split(","))) for x in open("a05_input.txt").read().splitlines()]

def points(lines):
    def drawline(x1,y1,x2,y2):
        dx = np.sign(x2-x1)
        dy = np.sign(y2-y1)
        x = x1
        y = y1
        while True:
            canvas[x,y] += 1
            x += dx
            y += dy
            if x == x2 and y == y2:
                canvas[x,y] += 1
                break

    canvas = np.zeros((1000,1000))
    for line in lines:
        drawline(*line)
    print((canvas > 1).sum())


straights = [a for a in lines if a.x1 == a.x2 or a.y1 == a.y2]
points(straights)
points(lines)