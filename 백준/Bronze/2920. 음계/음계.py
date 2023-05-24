a = [i for i in range(1, 9)]
d = sorted(a, reverse=True)
lst = list(map(int, input().split()))
ans = 'mixed'
if lst == a:
    ans = 'ascending'
if lst == d:
    ans = 'descending'
print(ans)
