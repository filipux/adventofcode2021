row = "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"


row = [x if not x.isdigit() else int(x) for x in row]

def findleftindex(row,i):
    while True:
        i -= 1
        if i <= 0:
            return -1
        if str(row[i]).isdigit():
            return i

def findrightindex(row,i):
    while True:
        i += 1
        if i >= len(row):
            return -1
        if str(row[i]).isdigit():
            return i

def explode(row):
    i = 0
    while i < len(row)-2:
        a,b,c = row[i:i+3]
        if str(a).isdigit() and b == "," and str(c).isdigit():
            
            left = findleftindex(row,i)
            if left >= 0:
                row[left] += a
            
            right = findrightindex(row,i+2)
            if right >= 0:
                row[right] += c
            
            row = row[:i-1] + [0] + row[i+4:]

        i += 1
    return row
            
def split(row):
    i=0
    while i < len(row):
        #print(row[i])
        if str(row[i]).isdigit():
            if row[i] >= 10:
                row = row[:i] + ["[", row[i]//2 , ",", row[i]//2 + (row[i] % 2 > 0), "]"] + row[i+1:]
                #print("NYYYY", "".join(map(str, row)))
        i += 1
    return row
          
#print("".join(map(str, row)))
#row = explode(row)
#print("".join(map(str, row)))
print("".join(map(str, row)))  
row = explode(row)
print("".join(map(str, row)))
row = split(row)
print("".join(map(str, row)))
#row = split(row)
#print("".join(map(str, row)))
