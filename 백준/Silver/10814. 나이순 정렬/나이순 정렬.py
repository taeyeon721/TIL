N = int(input())
lst = []
for _ in range(N):
    age, name = map(str, input().split())
    lst.append([int(age), name])
lst = sorted(lst, key=lambda x: x[0])
for i in range(N):
    print(*lst[i])