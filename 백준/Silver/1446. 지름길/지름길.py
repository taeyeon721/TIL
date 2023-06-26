N, D = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
arr = [i for i in range(D+1)]
for i in range(D+1):
    arr[i] = min(arr[i], arr[i-1]+1)
    for s, e, l in lst:
        if i == s and e <= D and arr[i]+l < arr[e]:
            arr[e] = arr[i]+l
print(arr[D])