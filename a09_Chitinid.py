import numpy as np
lines = open("a09_input.txt").read().splitlines()

# Part 1

nums = np.array([list(map(int, x)) for x in lines])
valid = []
m, n = nums.shape

def neighbors(x, y):
    out = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(a, b) for a, b in out if 0 <= a < m and 0 <= b < n]

minimums = {
    (x, y) for x in range(m) for y in range(n)
    if all(nums[cx, cy] > nums[x, y] for cx, cy in neighbors(x, y))
}
print(sum(nums[x, y] + 1 for x, y in minimums))




# Part 2

def area(loc):
    x, y = loc
    if nums[x, y] in {-1, 9}:
        return 0
    nums[x, y] = -1
    return 1 + sum(map(area, neighbors(x, y)))


print(np.prod(sorted(map(area, minimums))[-3:]))