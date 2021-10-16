import sys
from collections import deque
import copy

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

List = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
ans = 0
def bfs():
    dq = deque()
    temp = copy.deepcopy(List)
    for yy in range(N):
        for xx in range(M):
            if temp[yy][xx] == 2:
                dq.append([yy, xx])
    while(dq):
        y, x = dq.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < N and 0 <= xx < M and temp[yy][xx] == 0:
                temp[yy][xx] = 2
                dq.append([yy, xx])
    zero_cnt = 0
    for y in range(N):
        for x in range(M):
            if temp[y][x] == 0:
                zero_cnt += 1
    return zero_cnt

def dfs(y, x, level):
    global ans
    if level == 2:
        ans = max(ans ,bfs())
        return

    for yy in range(N):
        for xx in range(M):
            if List[yy][xx] == 0:
                List[yy][xx] = 1
                dfs(yy, xx, level + 1)
                List[yy][xx] = 0

for y in range(N):
    for x in range(M):
        if List[y][x] == 0:
            List[y][x] = 1
            dfs(y, x, 0)
            List[y][x] = 0

print(ans)