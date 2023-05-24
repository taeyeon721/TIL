T = int(input())
cntA, cntB, cntC = 0, 0, 0
while T > 0:
    if T % 10 != 0:
        break
    if T >= 300:
        T -= 300
        cntA += 1
    elif T >= 60:
        T -= 60
        cntB += 1
    else:
        T -= 10
        cntC += 1
if cntA == 0 and cntB == 0 and cntC == 0:
    print(-1)
else:
    print(f'{cntA} {cntB} {cntC}')