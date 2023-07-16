import sys
input = sys.stdin.readline

N = int(input())
lst = []
dic = {}

for i in range(N):
    n = int(input())
    lst.append(n)
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1
lst = sorted(lst)
mean = round(sum(lst)/N)
print(mean)
median = lst[N//2]
print(median)
mode = [k for k, v in dic.items() if max(dic.values()) == v]
mode = sorted(mode)
if len(mode) > 1:
    print(mode[1])
else:
    print(mode[0])
r = lst[N-1]-lst[0]
print(r)