from math import *
a, b = 2, 4
def solve(a, b):
    ans = 1
    for i in range(1, b + 1):
        ans *= (a - i + 1)
        ans /= i
    return ans


print(comb(b, a))
print(solve(b, a))
