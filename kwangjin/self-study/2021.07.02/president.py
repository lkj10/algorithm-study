import sys
sys.stdin = open("input.txt", "r")

N = int(sys.stdin.readline())
List = [[50]*(N+1) for _ in range(N+1)]
res = []

while 1:
    A, B = map(int, sys.stdin.readline().split())
    if A == -1 and B == -1:
        break
    List[A][B] = 1
    List[B][A] = 1

for i in range(N+1):
    List[i][i] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            List[i][j] = min(List[i][j], List[i][k] + List[k][j])


for i in range(1, N+1):
    MAX = 0
    for j in range(1, N+1):
        if List[i][j] > MAX:
            MAX = List[i][j]
    res.append(MAX)
cnt = 0
out = []
for i in range(N):
    if min(res) == res[i]:
        cnt += 1
        out.append(i)

print(min(res), cnt)
for i in out:
    print(i+1, end =' ')
        
