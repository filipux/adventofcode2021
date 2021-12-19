edges = [tuple(x.split("-")) for x in open("a12_input.txt").read().splitlines()]
paths = {v:[] for v in sum(edges, ())}

for v in paths:
    paths[v] += [b for a,b in edges if a == v]
    paths[v] += [a for a,b in edges if b == v]

def explore(cave, history=[]):
    if cave == "end":
        return [history + [cave]]
    else:
        out = []
        for v in paths[cave]:
            if not v in filter(str.islower, history):
                out += explore(v, history + [cave])
        return out

print(len(explore("start")))


def explore2(cave, history=[]):
    if cave == "end":
        return [history + [cave]]
    else:
        out = []
        for v in paths[cave]:
            smallCaves = list(filter(str.islower, history + [cave]))
            hasDups = len(smallCaves) - len(set(smallCaves)) > 1
            if not hasDups and v != "start":
                out += explore2(v, history + [cave])
        return out

print(len(explore2("start")))