N = int(input())
lst = set()
for i in range(N):
    lst.add(input())
lst = list(lst)
lst.sort()
lst = sorted(lst, key=len)
for st in lst:
    print(st)