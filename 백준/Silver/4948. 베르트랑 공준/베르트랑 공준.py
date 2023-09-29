import sys
input = sys.stdin.readline
lst = [1]*(123457*2)
lst[0] = 0
lst[1] = 0
for i in range(2, 123457):
    for j in range(2*i, 2*123457, i):
        if lst[j] == 1:
            lst[j] = 0
while True:
    n = int(input())
    if n == 0:
        break
    cnt = lst[n+1:2*n+1]
    print(cnt.count(1))