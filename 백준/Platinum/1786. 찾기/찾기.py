import sys
input = sys.stdin.readline
T = input().rstrip()
P = input().rstrip()
lst = [0]*len(P)
i = 0
ans = []
for j in range(1, len(P)):
    while i > 0 and P[i] != P[j]:
        i = lst[i-1]
    if P[i] == P[j]:
        i += 1
        lst[j] = i
i = 0
for j in range(len(T)):
    while i > 0 and P[i] != T[j]:
        i = lst[i-1]
    if P[i] == T[j]:
        i += 1
        if i == len(P):
            ans.append(j-i+2)
            i = lst[i-1]
print(len(ans))
print(*ans)