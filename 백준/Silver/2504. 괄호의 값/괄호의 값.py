st = input()
stack = []
ans = 0
tmp = 1
for i in range(len(st)):
    if st[i] == '(':
        stack.append(st[i])
        tmp *= 2
    elif st[i] == '[':
        stack.append(st[i])
        tmp *= 3
    elif st[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if st[i-1] == '(':
            ans += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if st[i-1] == '[':
            ans += tmp
        stack.pop()
        tmp //= 3
if stack:
    ans = 0
print(ans)