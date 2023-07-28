from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    D = [0]+list(map(int, input().split()))
    adj = [[] for _ in range(N+1)]
    visited = [0]*(N+1)
    for _ in range(K):
        x, y = map(int, input().split())
        adj[x].append(y)
        visited[y] += 1
    q = deque()
    dp = [0]*(N+1)
    for i in range(1, N+1):
        if visited[i] == 0:
            dp[i] = D[i]
            q.append(i)
    while q:
        i = q.popleft()
        for ni in adj[i]:
            visited[ni] -= 1
            dp[ni] = max(dp[i]+D[ni], dp[ni])
            if visited[ni] == 0:
                q.append(ni)
    W = int(input())
    print(dp[W])