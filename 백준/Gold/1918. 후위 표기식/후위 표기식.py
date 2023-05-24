pri = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 4}

st = input()
equ = ''
stk = []
# [1] 중위 표기 -> 후위 표기식으로 변경
for i in range(len(st)):
    if st[i] not in pri:
        equ += st[i]
    elif st[i] == ')':
        if i == len(st)-1:
            break
        while stk[-1] != '(':
            equ += stk.pop()
        stk.pop()
    else:
        if len(stk) == 0 or st[i] == '(':
            stk.append(st[i])
        else:
            while stk and stk[-1] != '(' and pri[stk[-1]] >= pri[st[i]]:
                equ += stk.pop()
            stk.append(st[i])

while len(stk) > 0:  # 스택에 데이터 있다면
    if stk[-1] == '(':
        stk.pop()
    else:
        equ += stk.pop()

print(equ)