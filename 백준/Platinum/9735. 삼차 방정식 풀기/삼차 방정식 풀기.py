N = int(input())
for _ in range(N):
    ans = set()
    x1 = 0
    A, B, C, D = map(int, input().split())

    for i in range(2000001):
        if A*(i**3)+B*(i**2)+C*i+D == 0:
            x1 = i
            ans.add(i)
            break
        if -A*(i**3)+B*(i**2)-C*i+D == 0:
            x1 = -i
            ans.add(-i)
            break
    B = B+A*x1
    C = C+B*x1

    if B**2-4*A*C >= 0:
        x2 = (-B-(B**2-4*A*C)**(1/2))/(2*A)
        ans.add(x2)
        x3 = (-B+(B**2-4*A*C)**(1/2))/(2*A)
        ans.add(x3)
    ans = list(ans)
    ans.sort()
    print(*ans)