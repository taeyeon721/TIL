H, M = map(int, input().split())
if M < 45:
    H, M = (H-1)%24, M+60
print(f'{H} {M-45}')