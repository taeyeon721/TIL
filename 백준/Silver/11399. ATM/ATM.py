import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
lst.sort()
ans = [0]*N
ans[0] = lst[0]
for i in range(1, N):
    ans[i] = ans[i-1]+lst[i]
print(sum(ans))