import sys
input = sys.stdin.readline
N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
ans = []
visited = [0]*N


def f():
    if len(ans) == M:
        print(*ans)
        return
    n = 0
    for i in range(N):
        if lst[i] != n and visited[i] == 0:
            ans.append(lst[i])
            visited[i] = 1
            n = lst[i]
            f()
            ans.pop()
            visited[i] = 0


f()