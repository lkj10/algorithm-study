import sys
sys.stdin = open("input.txt", "r")

n, m = map(int, sys.stdin.readline().split())
List = [[10000000]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    List[i][i] = 0

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    List[a][b] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            List[i][j] = min(List[i][j], List[i][k] + List[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if List[i][j] == 10000000:
            List[i][j] = 'M'
