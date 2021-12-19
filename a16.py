import numpy as np

hex = open("a16_input.txt").read().splitlines()[0]
#hex = "38006F45291200"
#hex = "04005AC33890"
bin = "".join([format(int(x, 16), '0>4b') for x in hex])


p = 0
def read(num):
    global p
    p += num
    return bin[p-num:p]

def readint(num):
    return int(read(num), 2)


versiontotal = 0
def readpackage():
    global versiontotal
    version = readint(3)
    type = readint(3)
    versiontotal += version
    print("version", version, ", type", type)
    if type == 4:
        print("literal")
        vstr = ""
        while True:
            b = readint(1)
            vstr += read(4)
            if not b: break
        value = int(vstr,2)
        print(value)
        return value
    else:
        values = []
        if readint(1) == 0:
            sub_bits = readint(15)
            print("Sub data bits", sub_bits)
            pend = p + sub_bits
            while p < pend:
                values.append(readpackage())
        else:
            sub_count = readint(11)
            print("sub count", sub_count)
            for _ in range(sub_count):
                values.append(readpackage())
        
        if type == 0: return sum(values)
        elif type == 1: return np.prod(values)
        elif type == 2: return min(values)
        elif type == 3: return max(values)
        elif type == 5: return int(values[0] > values[1])
        elif type == 6: return int(values[0] < values[1])
        elif type == 7: return int(values[0] == values[1])
        else:
            print("NOOOOOOOOOOOOOO")
        
        

value = readpackage()
print(value)
print("versiontotal", versiontotal)