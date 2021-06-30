import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def DFS(x, y):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if N > xx >= 0 and M > yy >= 0 and visit[xx][yy] == 0 and List[xx][yy] == 1:
            visit[xx][yy] = 1
            DFS(xx, yy)


for _ in range(T):
    M, N, K = map(int, input().split())
    List = [[0]*M for i in range(N)]
    visit = [[0]*M for i in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        List[y][x] = 1
    for i in range(N):
        for j in range(M):
            if List[i][j] == 1 and visit[i][j] == 0:
                visit[i][j] = 1
                cnt += 1
                DFS(i, j)
    print(cnt)
