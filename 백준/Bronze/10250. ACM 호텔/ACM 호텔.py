T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    Y = N%H
    if Y == 0:
        Y = H
        X = N//H
    else:
        X = N//H + 1
    print(str(Y)+('0' + str(X) if X < 10 else str(X)))