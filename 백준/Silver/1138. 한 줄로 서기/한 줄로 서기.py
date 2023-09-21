N = int(input())
lst = list(map(int, input().split()))
ans = [0]*N
for i in range(N):
    k = lst[i]
    cnt = 0
    for j in range(N):
        if cnt == k and ans[j] == 0:
            ans[j] = i+1
            break
        elif ans[j] == 0:
            cnt += 1
print(*ans)