from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
q = deque([])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append([i, j])
            visited[i][j] = 0
            while q:
                i, j = q.popleft()
                for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<n and 0<=nj<m:
                        if arr[ni][nj] == 1:
                            if visited[ni][nj] == 0:
                                visited[ni][nj] = visited[i][j]+1
                                q.append([ni, nj])
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1
for i in range(n):
    print(*visited[i])