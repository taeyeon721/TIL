import sys
input = sys.stdin.readline
lst = list(map(ord, input().upper()))
cnt = [0]*65+[lst.count(i) for i in range(65, 91)]
ans = [i for i, value in enumerate(cnt) if value == max(cnt)]
if len(ans) > 1:
    print('?')
else:
    print(chr(ans[0]))