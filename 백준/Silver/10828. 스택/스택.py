import sys
input = sys.stdin.readline
N = int(input())
stack = []
for _ in range(N):
    x = list(input().rstrip().split())
    if x[0] == "push":
        stack.append(x[1])
    elif x[0] == "pop":
        if stack:
            n = stack.pop()
            print(n)
        else:
            print(-1)
    elif x[0] == "size":
        print(len(stack))
    elif x[0] == "empty":
        print(0 if stack else 1)
    else:
        print(stack[-1] if stack else -1)