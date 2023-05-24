N = int(input())
lst = [[0]*10 for _ in range(101)]
for i in range(1, 10):
    lst[1][i] = 1
for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            lst[i][j+1] += lst[i-1][j]
        elif j == 9:
            lst[i][j-1] += lst[i-1][j]
        else:
            lst[i][j-1] += lst[i-1][j]
            lst[i][j+1] += lst[i-1][j]
print(sum(lst[N])%1000000000)
