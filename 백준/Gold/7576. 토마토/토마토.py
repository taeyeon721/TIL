from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
q = deque([])
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
t = 0
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append([i, j, t])
while q:
    i, j, t = q.popleft()
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < M:
            if box[ni][nj] == 0:
                box[ni][nj] = 1
                q.append([ni, nj, t+1])
for lst in box:
    if 0 in lst:
        t = -1
print(t)