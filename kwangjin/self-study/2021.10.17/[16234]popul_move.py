import sys
from collections import deque
from time import sleep
sys.stdin = open("input.txt", "r")

N, L, R = map(int, input().split())
List = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visit = [[0]*N for _ in range(N)]
day = 0

def bfs(dq, cnt):
    while dq:
        y, x = dq.popleft()
        visit[y][x] = cnt
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < N and 0 <= xx < N and L <= abs(List[yy][xx] - List[y][x]) <= R and visit[yy][xx] == 0:
                dq.append([yy, xx])
                SUM_List[cnt-1][0] += List[yy][xx]
                SUM_List[cnt-1][1] += 1
                visit[yy][xx] = cnt


while 1:
    flag = 0
    SUM_List = []
    cnt = 1
    for y in range(N):
        for x in range(N):
            if visit[y][x] == 0:
                dq = deque()
                SUM_List.append([List[y][x], 1])
                visit[y][x] = cnt
                for i in range(4):
                    yy = y + dy[i]
                    xx = x + dx[i]
                    if 0 <= yy < N and 0 <= xx < N and L <= abs(List[yy][xx] - List[y][x]) <= R and visit[yy][xx] == 0:
                        flag = 1
                        dq.append([yy, xx])
                        SUM_List[cnt-1][0] += List[yy][xx]
                        SUM_List[cnt-1][1] += 1
                        visit[yy][xx] = cnt
                bfs(dq, cnt)
                cnt += 1
    if flag == 0:
        print(day)
        break
    day += 1
    for y in range(N):
        for x in range(N):
            List[y][x] = int(SUM_List[visit[y][x]-1][0]/SUM_List[visit[y][x]-1][1])
    visit = [[0]*N for _ in range(N)]
