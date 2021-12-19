import numpy as np
import re

r = open("a17_input.txt").read()
x1,x2,y1,y2 = [int(x) for x in re.findall("[-\d]+", r)]

xvel = 0
yvel = 0

best = []

def run(xvel_start, yvel_start):
    xvel = xvel_start
    yvel = yvel_start
    x=0
    y=0

    ymax = y
    while x <= 300 and y >= -75:
        x += xvel
        y += yvel
        if xvel > 0: xvel -= 1
        if xvel < 0: xvel += 1
        yvel -= 1

        ymax = max(y, ymax)

        if x in range(x1, x2+1) and y in range(y1,y2+1):
            best.append((ymax,xvel_start, yvel_start))
            x = 10000000

for xvel_start in range(-100,300):
    for yvel_start in range(-100,200):
        run(xvel_start, yvel_start)    
       

print(max([y[0] for y in best]))
print(len(best))