from collections import deque
import sys
input = sys.stdin.readline


def bfs(board, start):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()
    q = deque([(start, 0, set())])
    while q:
        (r, c), cnt, s = q.popleft()
        if s == set(range(1, 7)):
            return cnt
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 5 and 0 <= nc < 5:
                if board[nr][nc] != -1:
                    ns = s.copy()
                    if board[nr][nc] != 0:
                        ns.add(board[nr][nc])
                    if (nr, nc, tuple(sorted(ns))) not in visited:
                        visited.add((nr, nc, tuple(sorted(ns))))
                        q.append(((nr, nc), cnt + 1, ns))
    return -1


board = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
ans = bfs(board, (r, c))
print(ans)