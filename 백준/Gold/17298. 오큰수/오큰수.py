import sys
input = sys.stdin.readline
# 왼쪽에서부터 스택에 저장하고 현재 수가 스택에 있는것보다 크면
# 스택이 빌 때까지 꺼내주고 지금 수를 저장
N = int(input())
A = list(map(int, input().split()))
ans = [-1]*N
stack = [0]
for i in range(1, N):
    while stack and A[i] > A[stack[-1]]:
        ans[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)
print(*ans)