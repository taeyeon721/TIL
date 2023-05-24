_ = int(input())
V = input()
if V.count('A') > V.count('B'):
    print('A')
elif V.count('A') < V.count('B'):
    print('B')
else:
    print('Tie')