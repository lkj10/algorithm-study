import sys
import copy
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

Map = [list(map(int, input().split())) for _ in range(N)]
cloud = [[0]*N for _ in range(N)]


def move(dir, vector):
    for y in range(N):
        for x in range(N):
            if cloud[y][x] == 1:
                yy = (y + dy[dir]*vector) % N
                xx = (x + dx[dir]*vector) % N
                temp_cloud[yy][xx] = cloud[y][x]

    for y in range(N):
        for x in range(N):
            if temp_cloud[y][x] == 1:  # 비구름이면
                Map[y][x] += 1

    for y in range(N):
        for x in range(N):
            if temp_cloud[y][x] == 1:  # 비구름이면
                for i in range(1, 8, 2):
                    yy = y + dy[i]
                    xx = x + dx[i]
                    if 0 <= yy < N and 0 <= xx < N and Map[yy][xx] > 0:
                        Map[y][x] += 1

    for y in range(N):
        for x in range(N):
            if temp_cloud[y][x] == 0 and Map[y][x] > 1:  # 비구름이면
                temp_cloud[y][x] = 1
                Map[y][x] -= 2
            elif temp_cloud[y][x] == 1:  # 이미 1이면 안됨
                temp_cloud[y][x] = 0


cloud[N-1][0], cloud[N-2][0] = 1, 1  # 비구름 생성
cloud[N-1][1], cloud[N-2][1] = 1, 1


for _ in range(M):
    d, s = map(int, input().split())
    temp_cloud = [[0]*N for _ in range(N)]
    move(d-1, s)
    cloud = copy.deepcopy(temp_cloud)

ans = 0
for y in range(N):
    for x in range(N):
        ans += Map[y][x]

print(ans)
