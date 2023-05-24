def inorder(n):
    global w, d
    if n:
        d += 1
        inorder(ch1[n])
        w += 1
        loc[n] = w
        height[n] = d
        inorder(ch2[n])
        d -= 1


def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:
            return i


N = int(input())
ch1 = [0]*(N+1)
ch2 = [0]*(N+1)
par = [0]*(N+1)
loc = [0]*(N+1)
height = [0]*(N+1)
w = 0
d = 0
for _ in range(N):
    a, b, c = map(int, input().split())
    if b > 0:
        ch1[a] = b
        par[b] = a
    if c > 0:
        ch2[a] = c
        par[c] = a
root = find_root(N)
inorder(root)
max_height = 0
for h in height:
    if h > max_height:
        max_height = h
maxW = 1
maxL = 1
for i in range(2, max_height+1):
    max_loc = 1
    min_loc = N
    for j in range(N+1):
        if height[j] == i and loc[j] > max_loc:
            max_loc = loc[j]
        if height[j] == i and loc[j] < min_loc:
            min_loc = loc[j]
    if maxW < max_loc - min_loc + 1:
        maxW = max_loc - min_loc + 1
        maxL = i
print(f'{maxL} {maxW}')