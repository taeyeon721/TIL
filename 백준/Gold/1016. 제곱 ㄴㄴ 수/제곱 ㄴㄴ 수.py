n, m = map(int, input().split())
lst = [0]*(m-n+1)
for i in range(2, int(m**(1/2))+1):
    x = i**2
    for j in range(-(n%x), m-n+1, i**2):
        if j >= 0:
            lst[j] = 1
print(lst.count(0))