import sys
from collections import deque
import heapq
import copy
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
List = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(y, x):
    global g_cnt
    dq = deque([[y, x]])
    local_y, local_x = y, x
    list_cnt = [0]*5 # 1. 크기, 2. 무지개 블록 수, 3. 행, 4. 열 (다 음수로)
    list_cnt[0] -= 1
    while dq :
        y, x = dq.popleft()
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < N and 0 <= xx < N and List[yy][xx] != -1 and List[yy][xx] != -2 and Group[yy][xx] == 0 :
                if List[yy][xx] == 0 :
                    list_cnt[1] -= 1
                    list_cnt[0] -= 1
                elif List[yy][xx] == List[local_y][local_x] :
                    list_cnt[0] -= 1
                else:
                    continue
                Group[yy][xx] = g_cnt
                dq.append([yy, xx])
    for y in range(N):
        for x in range(N):
            if List[y][x] == 0:
                Group[y][x] = 0

    for y in range(N):
        for x in range(N):
            if Group[y][x] == g_cnt and List[y][x] != 0:
                list_cnt[2] = -y
                list_cnt[3] = -x
                list_cnt[4] = g_cnt
                heapq.heappush(hq, list_cnt)
                return

def delete():
    global ans
    if hq :
        pass
    else:
        return -1
    a, b, c, d, e = heapq.heappop(hq)
    if a > -2  :
        return -1
    dq = deque([[-c, -d]])
    visit = [[0]*N for _ in range(N)]
    while dq :
        y, x = dq.popleft()
        visit[y][x] = 1
        for i in range(4):
            yy = y + dy[i]
            xx = x + dx[i]
            if 0 <= yy < N and 0 <= xx < N and List[yy][xx] != -1 and List[yy][xx] != -2 and (Group[yy][xx] == 0 or Group[yy][xx] == e) and visit[yy][xx] == 0:               
                visit[yy][xx] = 1
                Group[yy][xx] = e
                dq.append([yy, xx])

    ans += pow(a, 2)
    for y in range(N):
        for x in range(N):
            if Group[y][x] == e: # g_cnt와 같으면
                List[y][x] = -2 # -2 => 없는 칸


def gravity():
    for x in range(N):
        dq = deque()
        for y in range(N-1, -1, -1):
            if List[y][x] == -1:
                dq = deque()
            elif List[y][x] == -2:
                dq.append([y, x])
            elif dq:
                yy, xx = dq.popleft()
                List[yy][xx] = List[y][x]
                List[y][x] = -2
                dq.append([y, x])


def rotate_90():
    for x in range(N-1, -1, -1):
        for y in range(N):
            temp_List[N-x -1][y] = List[y][x]


ans = 0
while 1:
    g_cnt = 1
    hq = []
    Group = [[0]*N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            if List[y][x] > 0 and Group[y][x] == 0: # 일반 블록이면
                Group[y][x] = g_cnt
                bfs(y, x)
                g_cnt += 1
    if delete() == -1:
        break
    gravity()
    temp_List = [[0]*N for _ in range(N)]
    rotate_90()
    List = copy.deepcopy(temp_List)
    gravity()

print(ans)