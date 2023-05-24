T = int(input())
for tc in range(T):
    R, S = map(str, input().split())
    ans = ''
    for i in range(len(S)):
        ans += S[i]*int(R)
    print(ans)