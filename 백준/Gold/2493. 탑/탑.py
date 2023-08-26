import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
ans = [0]*N
stack = []
for i in range(N):
    while stack and lst[i] > lst[stack[-1]]:
        n = stack.pop()
    ans[i] = stack[-1]+1 if stack else 0
    stack.append(i)
print(*ans)