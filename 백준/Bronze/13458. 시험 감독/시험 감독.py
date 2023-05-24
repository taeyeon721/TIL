N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0
for n in A:
    n = n-B
    cnt += 1
    if n > 0:
        cnt += n // C
        if n % C:
            cnt += 1
print(cnt)