def preorder(n):
    if n:
        print(node_re.get(n), end='')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n:
        inorder(ch1[n])
        print(node_re.get(n), end='')
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(node_re.get(n), end='')


N = int(input())
ch1 = ['']*(N+1)
ch2 = ['']*(N+1)
node = {'A': 1,'B': 2,'C': 3,'D': 4,'E': 5,'F': 6,'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11,
        'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,'S': 19,'T': 20, 'U': 21,
        'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
node_re = {v:k for k,v in node.items()}
for i in range(N):
    p, c1, c2 = map(str, input().split())
    if c1 != '.':
        ch1[node[p]] = node[c1]
    if c2 != '.':
        ch2[node[p]] = node[c2]

preorder(1)
print()
inorder(1)
print()
postorder(1)