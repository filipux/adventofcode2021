lines = open("a04_input.txt").read().split("\n\n")
nums = [int(n) for n in lines.pop(0).split(",")]
boards = [[[(int(u), False) for u in t.split(" ") if u != ''
            ] for t in s.splitlines()
            ] for s in lines]
wins = []
scores = []
for num in nums:
    for board in boards:
        for row in board:
            for it, tile in enumerate(row):
                if tile[0] == num:
                    row[it] = (tile[0], True)
                    isBingoRow = len([v for v in row if v[1] == True]) == 5
                    isBingoCol = len([r[it][1] for r in board if r[it][1] == True]) == 5
                    if isBingoRow or isBingoCol:
                        if not board in wins:
                            wins.append(board)
                            unmarked = [v[0] for v in [item for r in board for item in r] if v[1] == False]
                            scores.append(sum(unmarked) * num)
                            
print("First:", scores[0])
print("Last:", scores[-1])