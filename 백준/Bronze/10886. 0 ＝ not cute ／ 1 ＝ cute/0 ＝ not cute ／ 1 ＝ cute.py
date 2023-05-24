N = int(input())
cnt = 0
for _ in range(N):
    z = int(input())
    if z == 0:
        cnt += 1
if cnt > N//2:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')