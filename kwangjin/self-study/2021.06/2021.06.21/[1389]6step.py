import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

List = [[5000]*(N) for i in range(N)]
SUM = 0
MIN = 5000
for i in range(M):
    A, B = map(int, input().split())
    List[A-1][B-1] = 1
    List[B-1][A-1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            List[i][j] = min(List[i][j], List[i][k] + List[k][j])

for i in List:
    SUM = sum(i)
    if MIN > SUM:
        MIN = SUM
        answer = List.index(i) + 1

print(answer)
