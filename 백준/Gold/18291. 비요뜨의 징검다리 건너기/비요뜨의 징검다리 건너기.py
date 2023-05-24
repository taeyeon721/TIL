T = int(input())
for _ in range(T):
    N = int(input())
    if N == 1:
        print(1)
    else:
        print(pow(2, N-2, 10**9+7))