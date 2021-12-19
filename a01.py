lines = open("a01_input.txt").read().splitlines()
lines = [int(i) for i in lines]

increased = 0
for i in range(len(lines)-1):
    if(lines[i+1] > lines[i]):
        increased += 1

print("increased:", increased)

increased = 0
for i in range(len(lines)-3):
    s1 = lines[i+0] + lines[i+1] + lines[i+2]
    s2 = lines[i+1] + lines[i+2] + lines[i+3]
    if(s2 > s1):
        increased += 1

print("increased slide 3:", increased)