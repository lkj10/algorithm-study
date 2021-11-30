import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N = int(input())

Map = [list(map(int, input().split())) for _ in range(N)]
dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

MAX = 0

def bfs(y, x, h):
    dq = deque([(y, x)])
    while dq:
        _y, _x = dq.popleft()
        for i in range(4):
            yy = _y + dy[i]
            xx = _x + dx[i]
            if 0 <= yy < N and 0 <= xx < N and visit[yy][xx] == 0 and Map[yy][xx] > h :
                visit[yy][xx] = 1
                dq.append((yy, xx))

for h in range(max(map(max, Map))):
    cnt = 0
    visit = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if visit[y][x] == 0 and Map[y][x] > h:
                cnt += 1
                visit[y][x] = 1
                bfs(y, x, h)
    MAX = max(MAX, cnt)

print(MAX)