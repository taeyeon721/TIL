def solution(s):
    stack = []
    i = 0
    while i < len(s):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        i += 1
    if stack:
        return False

    return True