import sys
input = sys.stdin.readline
K = int(input())
lst = [int(input()) for _ in range(K)]
stack = []
for i in range(K):
    if lst[i] == 0:
        stack.pop()
    else:
        stack.append(lst[i])
print(sum(stack))