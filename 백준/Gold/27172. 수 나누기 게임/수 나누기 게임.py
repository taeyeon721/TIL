import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
score = [0]*1000001
used = [0]*1000001

for i in lst:
    used[i] = 1
for i in sorted(lst):
    for j in range(i*2, 1000001, i):
        if used[j]:
            score[i] += 1
            score[j] -= 1

for i in lst:
    print(score[i], end=' ')