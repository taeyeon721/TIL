import sys

input = sys.stdin.readline
N = int(input())
parent = list(map(int, input().split()))
M = int(input())
tree = [[] for _ in range(N)]
visited = [0]*N
s = 0
cnt = 0
for i in range(N):
    if parent[i] == -1:
        s = i
    elif i == M:
        continue
    else:
        tree[parent[i]].append(i)
stack = [s]

while stack:
    n = stack.pop()
    if n == M:
        continue
    if not visited[n]:
        visited[n] = 1
        if len(tree[n]) == 0:
            cnt += 1
        else:
            for i in range(len(tree[n])):
                if visited[tree[n][i]] == 0:
                    stack.append(tree[n][i])
print(cnt)