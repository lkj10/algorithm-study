import sys
sys.stdin = open("input.txt", "r")
N, M = map(int, input().split())

center_y = N//2
center_x = N//2
dy = [-1, 1, 0, 0]  # 위, 아래 왼쪽, 오른쪽
dx = [0, 0, -1, 1]  # 위, 아래 왼쪽, 오른쪽

Map = [list(map(int, input().split())) for _ in range(N)]
temp = []
boom = 0


def blizard(dir, vector):
    y, x = center_y, center_x
    for _ in range(vector):
        y += dy[dir]
        x += dx[dir]
        Map[y][x] = 0


def last_num_check():
    last_num = 0
    y, x = center_y, center_x
    y += dy[2]
    x += dx[2]
    while(1):
        last_num += 1
        for _ in range(last_num):  # 왼쪽
            if Map[y][x] == 0:
                return y, x
            if last_num == 1:
                continue
            y += dy[2]
            x += dx[2]
        for _ in range(last_num):  # 아래
            if Map[y][x] == 0:
                return y, x
            y += dy[1]
            x += dx[1]

        last_num += 1

        for _ in range(last_num):  # 오른쪽
            if Map[y][x] == 0:
                return y, x
            y += dy[3]
            x += dx[3]

        for _ in range(last_num):  # 위
            if Map[y][x] == 0:
                return y, x
            y += dy[0]
            x += dx[0]


dir_cnt = 0


def tornado(last_y, last_x):
    global dir_cnt
    y, x = center_y, center_x
    while(1):
        dir_cnt += 1
        for _ in range(dir_cnt):  # 왼쪽
            if y == last_y and x == last_x:
                return

            y += dy[2]
            x += dx[2]
            if Map[y][x] != 0:
                temp.append([y, x, Map[y][x]])
        for i in range(dir_cnt):  # 아래
            if y == last_y and x == last_x:
                return
            y += dy[1]
            x += dx[1]
            if Map[y][x] != 0:
                temp.append([y, x, Map[y][x]])
        dir_cnt += 1

        for _ in range(dir_cnt):  # 오른쪽
            if y == last_y and x == last_x:
                return
            y += dy[3]
            x += dx[3]
            if Map[y][x] != 0:
                temp.append([y, x, Map[y][x]])

        for _ in range(dir_cnt):  # 위
            if y == last_y and x == last_x:
                return
            y += dy[0]
            x += dx[0]
            if Map[y][x] != 0:
                temp.append([y, x, Map[y][x]])


def temp_check():
    idx = 1
    cnt = 1
    while(1):
        if idx <= len(temp):
            break
        if temp[idx-1][2] == temp[idx][2]:
            cnt = 1
            while(idx <= len(temp)):
                if temp[idx-1][2] == temp[idx][2] and temp[idx][2] != 0:
                    cnt += 1
                    idx += 1
                elif temp[idx]
                break
        if cnt >= 4:
            idx -= cnt
            for i in (idx, idx+cnt):
                temp[i][2] = 0
        idx += 1


last_y, last_x = last_num_check()

for i in range(M):
    d, s = map(int, input().split())
    last_y, last_x = last_num_check()
    blizard(d-1, s)
    tornado(last_y, last_x)
    temp_check()

print(temp)
