def makeFishes(days):
    dicts = {}

    for _ in range(8):
        dicts[_] = initFishes.count(_)

    for _ in range(days):
        numOfZeros = dicts[0]
        for key in dicts:
            if (key != 0):
                dicts[key - 1] = dicts[key]
        dicts[6] = dicts[6] + numOfZeros
        dicts[8] = numOfZeros

    return sum(dicts.values())


with open("a06_input.txt") as _file:
    file_contents = _file.read()
    initFishes = [int(fc) for fc in file_contents.split(',')]

    print('Part1 sum:', makeFishes(80))
    print('Part2 sum:', makeFishes(256))
