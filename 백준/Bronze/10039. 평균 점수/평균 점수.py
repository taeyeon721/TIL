score = []
for _ in range(5):
    n = int(input())
    if n < 40:
        n = 40
    score += [n]
print(sum(score)//5)