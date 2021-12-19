lines = open("a10_input.txt").read().splitlines()

tok_start = "([{<"
tok_end =   ")]}>"

points1 = {')': 3,']': 57,'}': 1197, '>': 25137 }
points2 = {')': 1,']': 2,'}': 3, '>': 4 }

total1 = 0
scores = []
for row in lines:
    q = []
    for tok in row:
        if tok in tok_start:
            expected = tok_end[tok_start.index(tok)]
            q.append(expected)
        elif tok in tok_end:
            expected = q.pop()
            if tok != expected:
                #print(row, "- Expected %s, but found %s instead" % (expected, tok))
                total1 += points1[tok]
                q.clear()
                break
    if len(q) > 0:
        q.reverse()
        #print(row,"- Complete by adding", "".join(q))
        lineTotal = 0
        for x in q:
            lineTotal = lineTotal * 5 + points2[x]
        scores.append(lineTotal)
    

print("Points 1:", total1)
print("Points 2:", sorted(scores)[len(scores)// 2])