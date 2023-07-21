import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
left = 0
right = N-1
sol1 = lst[left]
sol2 = lst[right]
minV = abs(sol1+sol2)
while left < right:
    if minV > abs(lst[left]+lst[right]):
        sol1, sol2 = lst[left], lst[right]
        minV = abs(sol1+sol2)

    if lst[left]+lst[right] > 0:
        right -= 1
    else:
        left += 1
print(sol1, sol2)