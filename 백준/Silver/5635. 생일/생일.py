n = int(input())
lst = [input().split() for _ in range(n)]
lst = sorted(lst, key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(lst[n-1][0])
print(lst[0][0])
