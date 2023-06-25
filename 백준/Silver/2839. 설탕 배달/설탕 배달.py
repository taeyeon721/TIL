N = int(input())
lst = [-1]*5001
lst[3] = 1
lst[5] = 1
for i in range(6, N+1):
    if lst[i-3] != -1:
        lst[i] = lst[i-3]+1
    if lst[i-5] != -1:
        lst[i] = lst[i-5]+1
print(lst[N])