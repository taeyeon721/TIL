N, K = map(int, input().split())
ans = 1
if K > N//2:
    K = N-K
for i in range(N-K+1, N+1):
    ans *= i
for i in range(1, K+1):
    ans //= i
print(ans%10007)