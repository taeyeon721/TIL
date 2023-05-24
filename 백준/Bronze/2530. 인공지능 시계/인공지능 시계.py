A, B, C = map(int, input().split())
D = int(input())
H = D//3600
M = (D-H*3600)//60
S = D%60
if C+S >= 60:
    B += 1
if B+M >= 60:
    A += 1
print(f'{(A+H)%24} {(B+M)%60} {(C+S)%60}')