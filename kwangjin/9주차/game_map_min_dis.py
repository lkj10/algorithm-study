from collections import deque


def solution(maps):
    N = len(maps)
    M = len(maps[0])
    answer = 0
    visit = [[0]*M for _ in range(N)]
    visit[0][0] = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dq = deque()
    dq.append((0, 0))
    MAP = []
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if N > xx >= 0 and M > yy >= 0 and maps[xx][yy] == 1:
                maps[xx][yy] = 0
                visit[xx][yy] = visit[x][y] + 1
                dq.append((xx, yy))

    return visit[N-1][M-1] if visit[N-1][M-1] != 0 else -1
