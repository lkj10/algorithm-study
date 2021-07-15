import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    for i in range(N+1):
        if visit[i] == 0 and List[L][i] == 1:
            visit[i] = 1
            DFS(i)

N = int(sys.stdin.readline())
T = int(sys.stdin.readline())
List = [[0]*(N+1) for _ in range(N+1)]
visit = [0] * (N+1)

for _ in range(T):
    i, j = map(int, sys.stdin.readline().split())
    List[i][j] = 1
    List[j][i] = 1

DFS(1)
print(sum(visit)-1)
