A, B = map(int, input().split())
C = int(input())
if B+(C%60) >= 60:
    A += 1
B = (B+(C%60))%60
A = (A+(C//60))%24
print(f'{A} {B}')