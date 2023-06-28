T = int(input())
for _ in range(T):
    st = list(input())
    stack = []
    ans = "YES"
    for s in st:
        if s == '(':
            stack.append(s)
        if s == ')':
            if not stack:
                ans = "NO"
                break
            else:
                stack.pop()
    if len(stack) != 0:
        ans = "NO"
    print(ans)