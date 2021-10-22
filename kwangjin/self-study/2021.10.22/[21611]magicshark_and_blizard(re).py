import sys
from collections import deque
import copy
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
y, x = N//2, N//2
center_y, center_x = N//2, N//2
last_y, last_x = -1, -1

Map = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def tornado(dir):
    global y, x, last_y, last_x
    for i in range(dir_cnt):
        y += dy[dir]
        x += dx[dir]
        if y < 0 or x < 0:
            return -1
        if Map[y][x] == 0 and last_x == -1 and last_y == -1:
            last_x, last_y = x, y


def tornado2(dir):
    global y, x, last_y, last_x
    for i in range(dir_cnt):
        y += dy[dir]
        x += dx[dir]
        if y < 0 or x < 0:
            return -1
        if Map[y][x] != 0:
            dq.append(Map[y][x])


def tornado3(dir):
    global y, x
    for i in range(dir_cnt):
        if dq:
            val = dq.popleft()
            y += dy[dir]
            x += dx[dir]
            if y < 0 or x < 0:
                return -1
            temp_Map[y][x] = val
        else:
            return -1


def boom(d, s):
    global center_y, center_x
    y, x = center_y, center_x
    for _ in range(s):
        y += dy[d]
        x += dx[d]
        if 0 <= y < N and 0 <= x < N:
            Map[y][x] = 0


def check():
    global ans
    for a in range(len(dq)-1):
        if dq[a] == dq[a+1] and dq[a] != -1:
            cnt = 1
            for b in range(a+1, len(dq)):
                if dq[a] == dq[b]:
                    cnt += 1
                else:
                    break
            if cnt > 3:
                ans += cnt * dq[a]
                for b in range(a, a+cnt):
                    dq[b] = -1


def check2():
    temp = 0
    # for a in range(temp, len(dq)-1):
    #     if dq[a] == dq[a+1] and dq[a] != -1:
    #         cnt = 1
    #         for b in range(a+1, len(dq)):
    #             if dq[a] == dq[b]:
    #                 cnt += 1
    #             else:
    #                 break
    #         dq2.append(cnt)
    #         dq2.append(dq[a])
    #         temp += cnt
    #     else:
    #         dq2.append(1)
    #         dq2.append(dq[a])
    #     print(dq2, dq[a], cnt, a, temp)
    a = 0
    while len(dq) > a:
        cnt = 1
        if a < len(dq)-1 and dq[a] == dq[a+1] and dq[a] != -1:
            for b in range(a+1, len(dq)):
                if dq[a] == dq[b]:
                    cnt += 1
                else:
                    break
        dq2.append(cnt)
        dq2.append(dq[a])
        a += cnt


dir_cnt = 1

ans = 0
while(1):
    if tornado(2) == -1:
        break
    if tornado(1) == -1:
        break
    dir_cnt += 1
    if tornado(3) == -1:
        break
    if tornado(0) == -1:
        break
    dir_cnt += 1

for _ in range(M):
    d, s = map(int, input().split())
    dq = deque()
    boom(d-1, s)
    dir_cnt = 1
    y, x = N//2, N//2
    while(1):
        if tornado2(2) == -1:
            break
        if tornado2(1) == -1:
            break
        dir_cnt += 1
        if tornado2(3) == -1:
            break
        if tornado2(0) == -1:
            break
        dir_cnt += 1
    while(1):
        temp_dq = deque()
        len_check = len(dq)
        check()
        for i in dq:
            if i != -1:
                temp_dq.append(i)
        dq = copy.deepcopy(temp_dq)
        if len_check == len(dq):
            break
    temp_Map = [[0]*N for _ in range(N)]
    y, x = N//2, N//2
    dir_cnt = 1

    dq2 = deque()
    check2()
    dq = copy.deepcopy(dq2)
    while(1):
        if tornado3(2) == -1:
            break
        if tornado3(1) == -1:
            break
        dir_cnt += 1
        if tornado3(3) == -1:
            break
        if tornado3(0) == -1:
            break
        dir_cnt += 1
    Map = copy.deepcopy(temp_Map)

print(ans)
