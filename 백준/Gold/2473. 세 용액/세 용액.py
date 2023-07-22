import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
sol1, sol2, sol3 = 0, 0, 0
minV = 10**10
for i in range(N-2):
    j = i+1
    k = N-1
    while j < k:
        tmp = lst[i] + lst[j] + lst[k]
        if abs(tmp) < minV:
            minV = abs(tmp)
            sol1, sol2, sol3 = lst[i], lst[j], lst[k]

        if tmp < 0:
            j += 1
        else:
            k -= 1
print(sol1, sol2, sol3)