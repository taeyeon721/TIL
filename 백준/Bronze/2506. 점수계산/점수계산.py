N = int(input())
lst = list(map(int, input().split()))
cnt = 0
s = 0
for i in range(N):
    if lst[i] == 1:
        cnt += 1
        s += cnt
    else:
        cnt = 0
print(s)