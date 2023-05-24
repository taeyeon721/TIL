lst = []
M = int(input())
N = int(input())
i = int(M**(1/2))
while i**2 <= N:
    if i**2 >= M and i**2 <= N:
        lst.append(i**2)
        i += 1
    elif i**2 < M:
        i += 1
if len(lst):
    print(sum(lst))
    print(min(lst))
else:
    print(-1)
