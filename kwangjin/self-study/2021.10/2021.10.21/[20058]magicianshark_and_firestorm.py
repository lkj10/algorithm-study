import sys
import copy
from collections import deque
sys.stdin = open("input.txt", "r")

N, Q = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(pow(2, N))]
list_Q = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def foo(L):
    for y in range(0, pow(2, N), L):
        for x in range(0, pow(2, N), L):
            temp_list = [[0]*L for _ in range(L)]
            for yy in range(y, y + L):
                for xx in range(x, x + L):
                    temp_list[xx-x][L-(yy-y)-1] = Map[yy][xx]
            for yy in range(y, y + L):
                for xx in range(x, x + L):
                    Map[yy][xx] = temp_list[yy-y][xx-x]
    temp_Map = copy.deepcopy(Map)

    for y in range(pow(2, N)):
        for x in range(pow(2, N)):
            cnt = 0
            for i in range(4):
                yy = y + dy[i]
                xx = x + dx[i]
                if 0 <= yy < (pow(2, N)) and 0 <= xx < (pow(2, N)) and Map[yy][xx] > 0:
                    cnt += 1
            if cnt < 3:
                temp_Map[y][x] -= 1
                if temp_Map[y][x] < 0:
                    temp_Map[y][x] = 0
    
    return temp_Map


def bfs(y, x):
    global Max
    visit[y][x] = 1
    dq = deque([[y,x]])
    ice_cnt = 1
    while dq:
        yy, xx = dq.popleft()
        for i in range(4):
                yyy = yy + dy[i]
                xxx = xx + dx[i]
                if 0 <= yyy < (pow(2, N)) and 0 <= xxx < (pow(2, N)) and visit[yyy][xxx] == 0 and Map[yyy][xxx] > 0:
                    visit[yyy][xxx] = 1
                    dq.append([yyy, xxx])
                    ice_cnt += 1
    Max = max(Max, ice_cnt)



for i in range(Q):
    Map = copy.deepcopy(foo(pow(2, list_Q[i])))

visit = [[0]*pow(2, N) for _ in range(pow(2, N))]
ans = 0
Max = 0
for y in range(pow(2, N)):
    for x in range(pow(2, N)):
        ans += Map[y][x]
        if visit[y][x] == 0 and Map[y][x] > 0:
            bfs(y, x)

print(ans)
print(Max)