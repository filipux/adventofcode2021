import time
from random import randint, random, sample, choice


def run(program, digits):
    mem = {'w':0, 'x':0, 'y':0, 'z': 0}
    for p in program:
        op = p[0]
        a = p[1]
        if op == 'inp':
            mem[a] = digits.pop(0)
        else:
            v = p[2]
            b = mem[v] if v.isalpha() else int(v)
            if op == 'add':
                mem[a] = mem[a] + b 
            elif op == 'mul':
                mem[a] = mem[a] * b 
            elif op == 'div':
                mem[a] = mem[a] // b
            elif op == 'mod':
                mem[a] = mem[a] % b 
            elif op == 'eql':
                mem[a] = int(mem[a] == b)
    return mem


program = [tuple(x.split()) for x in open("a24_input.txt").read().splitlines()]


def solve(shouldMaximize):

    # f will be in range -7..17
    def digitclamp(f):
        return [9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,9,8,7,6,5,4,3,2,1][int(round(f-1)+8)]

    # evaluate how good a solution is
    def cost(digits):
        mem = run(program, digits[:])
        z =  mem['z']
        v = sum([float(digits[d])*0.1**(d+1) for d in range(14)]) #convert digits to float
        return z * (1/v) if shouldMaximize else z * v

    # magic numbers that seem to work
    CR = 0.1
    RR = 0.1
    F = 0.9
    NP = 30

    # create initial random population
    population = [[randint(1,9) for x in range(14)] for n in range(NP)]

    while True:
        for ix, x in enumerate(population):
            a,b,c = sample(population, 3)
            if x in [a,b,c]: continue
            
            y = x[:]
            for i in range(14):
                if random() < CR:
                    y[i] = digitclamp(a[i] + F * (b[i]  - c[i]))
                elif random() < RR:
                    y[i] = randint(1,9)
                
            cost_y = cost(y)
            cost_x = cost(x)
            if cost_y <= cost_x:
                population[ix] = y
                if cost_y == 0:
                    return "".join([str(d) for d in y ])

shouldMaximize =  "1" in str(input("Would you like to solve part 1 or part 2? "))
print("....this could take a LONG time, press Ctrl+C when you're happy....")
solutions = []

while True:
    x = solve(shouldMaximize)
    solutions.append(x)
    print("Best so far (top 3)", sorted(solutions, reverse=shouldMaximize)[0:3])
