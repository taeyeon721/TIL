N, r, c = map(int, input().split())
ans = 0
while N > 0:
    N -= 1
    if r < 2**N and c >= 2**N:
        ans += 2**(2*N)
        c -= 2**N
    elif r >= 2**N and c < 2**N:
        ans += 2**(2*N)*2
        r -= 2**N
    elif r >= 2**N and c >= 2**N:
        ans += 2**(2*N)*3
        r -= 2**N
        c -= 2**N
print(ans)