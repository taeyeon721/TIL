import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
q = deque([])
for _ in range(N):
    cmd = list(map(str, input().split()))
    if cmd[0] == 'push':
        q.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if q:
            n = q.popleft()
        else:
            n = -1
        print(n)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)