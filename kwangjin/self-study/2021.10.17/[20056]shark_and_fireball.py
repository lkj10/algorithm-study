import sys
import copy
sys.stdin = open("input.txt", "r")

N, M, K = map(int, input().split())
Map = [[0]*N for _ in range(N)] # 질량
visit = [[0]*N for _ in range(N)] # 몇 개 있는지
vector = [[0]*N for _ in range(N)] # 속력
dir = [[[] for _ in range(N)] for _ in range(N)]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    for y in range(N):
        for x in range(N):
            if visit[y][x] != 0:
                yy, xx = y, x
                for _ in range(vector[y][x]):
                    yy = (yy + dy[dir[y][x][0]])%N
                    xx = (xx + dx[dir[y][x][0]])%N
                temp_Map[yy][xx] += Map[y][x]
                temp_visit[yy][xx] += 1
                temp_vector[yy][xx] += vector[y][x]
                temp_dir[yy][xx].append(dir[y][x])

for _ in range(M):
    # r = 행, c = 열, m = 질량, s = 속도, d = 방향
    r, c, m, s, d = map(int, input().split())
    Map[r-1][c-1] = m
    visit[r-1][c-1] = 1
    vector[r-1][c-1] = s
    dir[r-1][c-1].append(d)

for i in Map:
    print(i)
print()

for _ in range(K):
    temp_Map = [[0]*N for _ in range(N)] # 질량
    temp_visit = [[0]*N for _ in range(N)] # 몇 개 있는지
    temp_vector = [[0]*N for _ in range(N)] # 속력
    temp_dir = [[[] for _ in range(N)] for _ in range(N)]
    move()
    Map = copy.deepcopy(temp_Map)
    visit = copy.deepcopy(temp_visit)
    vector = copy.deepcopy(temp_vector)
    dir = copy.deepcopy(temp_dir)
    for i in Map:
        print(i)
    print()