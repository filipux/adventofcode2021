import re


class Node:
    def __init__(self, value = None):
        self.left  = None
        self.right = None
        self.parent = None
        self.value = value
    def __str__(self):
        if self.value is not None:
            return str(self.value)
        return "[" + str(self.left) + "," + str(self.right) + "]"


def parse_snailfish(fish):
    def parse(node, row, p=0):
        if p not in range(len(row)): return
        if row[p] == '[':
            n = Node()
            node.left = n
            n.parent = node
            parse(n,row, p+1)
        elif row[p] == ',':
            n = Node()
            node.right = n
            n.parent = node
            parse(n,row, p+1)
        elif row[p] == ']':
            #if node.parent is None:print("KALABALAJS")
            parse(node.parent,row, p+1)
        else:
            v = ""
            while row[p].isdigit() :
                v += row[p]
                p += 1
            node.value = int(v)
            parse(node.parent, row,p)
    n = Node()
    parse(n,fish)
    return n

def getvaluenodes(node):
    list = []
    def blef(node):
        if node.value is not None:
            list.append(node)
        else:
            blef(node.left)
            blef(node.right)
    blef(node)
    return list


def split(tree):
    nodes = getvaluenodes(tree)
    for i, n in enumerate(nodes):
        if n.value is not None and n.value >= 10:
            n.left = Node()
            n.left.parent = n
            n.left.value = n.value // 2 

            n.right = Node()
            n.right.parent = n
            n.right.value = n.value //2 + (n.value % 2 > 0)
            
            n.value = None
            return True
    return False

def level(node):
    level = 0
    while node.parent is not None:
        node = node.parent
        level += 1
    return level

def explode(tree):
    nodes = getvaluenodes(tree)
    for i, n in enumerate(nodes):
        a = n.parent.left
        b = n.parent.right
        if a.value is not None and b.value is not None and level(a) >= 5:
            #print("level", a.level)
            #print("value", a.value)


            if i-1 >= 0:
                nodes[i-1].value += a.value
            if i+2 < len(nodes):
                nodes[i+2].value += b.value
            a.parent.left = None
            a.parent.right = None
            a.parent.value = 0
            return True
    return False

def add(node1, node2):
    n = Node()
    n.left = node1
    n.right = node2
    node1.parent = n
    node2.parent = n
    return n

def reduce(fish):
    while True:
        old = str(fish)
        if explode(fish):
            continue
        if split(fish):
            continue
        if old == str(fish):
            break

def magnitude(fish):
    if fish.value is not None:
        return fish.value
    else:
        return 3*magnitude(fish.left) + 2*magnitude(fish.right)

rows = open("a18_input.txt").read().splitlines()
total = parse_snailfish(rows[0])
for row in rows[1:]:
    fish = parse_snailfish(row)
    total = add(total, fish)
    reduce(total)

print(magnitude(total))


combs = [(a,b) for a in range(len(rows)) for b in range(len(rows)) if a != b]
magn = []
for (a,b) in combs:
    bajs = [parse_snailfish(row) for row in rows]
    prutt = add(bajs[a], bajs[b])
    reduce(prutt)
    magn.append(magnitude(prutt))

print(max(magn))