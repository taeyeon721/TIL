lst = []
for _ in range(7):
    N = int(input())
    if N % 2:
        lst.append(N)
if len(lst):
    print(sum(lst))
    print(min(lst))
else:
    print(-1)