p1start,p2start = [int(x[-1]) for x in open("a21_input.txt").read().splitlines()]

p1,p2 = (p1start, p2start)
p1score, p2score = (0,0)

dice = 0
rollcount = 0

def roll():
    global dice
    global rollcount
    rollcount += 1
    dice += 1
    if dice > 100: dice = 1
    return dice

def rollthree():
    return [roll(), roll(), roll()]

while True:
    r = rollthree()
    p1 += sum(r)
    p1 = 1+(p1-1) % 10
    p1score += p1
    print("Player 1 rolls", "+".join(map(str,r)), "and moves to space", p1, "for a total score of", p1score)
    if p1score >= 1000:
        break

    r = rollthree()
    p2 += sum(r)
    p2 = 1+(p2-1) % 10
    p2score += p2
    print("Player 2 rolls", "+".join(map(str,r)), "and moves to space", p2, "for a total score of", p2score)
    if p2score >= 1000:
        break

print("Part 1", min(p1score, p2score) * rollcount)


# ------- Part 2 --------

from collections import namedtuple
Player = namedtuple('Player', ['pos', 'score'])

def step(p, dice):
    pos = 1 + (p.pos + dice -1) % 10
    score = p.score + pos
    return Player(pos, score)

# all sum combinations of three quantum dice rolls
def alldicesums(): 
    sums = []
    for t1 in range(1,4):
        for t2 in range(1,4):
            for t3 in range(1,4):
                sums.append(t1+t2+t3)
    return sums

dicesums = alldicesums()
cache = {}

def play(p1, p2):
    if (p1,p2) in cache: return cache[(p1,p2)] # <---- magic

    wins1, wins2 = (0,0)

    for dice1 in dicesums: # player1
        p1new = step(p1, dice1)
        if p1new.score >= 21:
            wins1 += 1
        else:
            for dice2 in dicesums: # player2
                p2new = step(p2, dice2)
                if p2new.score >= 21:
                    wins2 += 1
                else:
                    w1, w2 = play(p1new, p2new)
                    wins1 += w1
                    wins2 += w2
    cache[(p1,p2)] = (wins1, wins2) # <---- magic
    return (wins1, wins2)


p1 = Player(p1start,0)
p2 = Player(p2start,0)
wins = play(p1, p2)

print("Part 2", max(wins))