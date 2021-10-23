import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
List = []

for _ in range(N):
    temp = list(map(int, input().split()))
    List.append(temp)

visit = [[0]*M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
res = 0
def dfs(y, x, level, SUM):
    global res
    if level == 3:
        res = max(res, SUM)
        return

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        if 0 <= yy < N and  0 <= xx < M and visit[yy][xx] == 0:
            if level == 1:
                visit[yy][xx] = 1
                dfs(y, x, level+1, SUM + List[yy][xx])
                visit[yy][xx] = 0
            visit[yy][xx] = 1
            dfs(yy, xx, level+1, SUM + List[yy][xx])
            visit[yy][xx] = 0

for y in range(N):
    for x in range(M):
        visit[y][x] = 1
        dfs(y, x, 0, List[y][x])
        visit[y][x] = 0
print(res)