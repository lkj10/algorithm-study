import sys
from collections import deque
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

List = [[0]*(N+1) for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    List[u-1][v-1] = 1
    List[v-1][u-1] = 1

visit = [0]*(N+1)
v
def dfs(y):
    for i in range(N):
        if List[y][i] == 1 and visit[i] == 0:
            visit[i] = 1
            dfs(i)

    return

ans = 0
for y in range(N):
    for x in range(N):
        if List[y][x] == 1 and visit[y] == 0:
            visit[y] = 1
            dfs(y)
            ans += 1

for i in visit:
    if i == 0:
        ans += 1

print(ans-1)