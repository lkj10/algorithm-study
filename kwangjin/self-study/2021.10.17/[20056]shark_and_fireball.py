import sys
import copy
sys.stdin = open("input.txt", "r")

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

def move():
    for y in range(N):
        for x in range(N):
            if visit[y][x] > 0:
                for i in range(len(dir[y][x])):
                    yy = (y + dy[dir[y][x][i]] * vec[y][x]) % N
                    xx = (x + dx[dir[y][x][i]] * vec[y][x]) % N
                    temp_Map[yy][xx] += Map[y][x]
                    temp_dir[yy][xx].append(dir[y][x][i])
                    temp_visit[yy][xx] += 1
                    temp_vec[yy][xx] += vec[y][x]

    for y in range(N):
        for x in range(N):
            if temp_visit[y][x] > 1:
                temp_Map[y][x] = temp_Map[y][x]//5
                if temp_Map[y][x] == 0:
                    temp_visit[y][x] = 0
                    continue
                temp_vec[y][x] = temp_vec[y][x] // temp_visit[y][x]
                odd, even = 0, 0
                for i in range(len(temp_dir[y][x])):
                    if temp_dir[y][x][i] % 2 == 0:
                        even = 1
                    else: 
                        odd = 1
                if odd + even == 1 :
                    temp_dir[y][x] = [0, 2, 4, 6]
                else:
                    temp_dir[y][x] = [1, 3, 5, 7]

N, M, K = map(int, input().split())

Map = [[0]*N for _ in range(N)]
visit = [[0]*N for _ in range(N)]
dir = [[[] for _ in range(N)] for _ in range(N)]
vec = [[0]*N for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    Map[r-1][c-1] = m
    visit[r-1][c-1] += 1
    dir[r-1][c-1].append(d)
    vec[r-1][c-1] = s

for _ in range(K):
    temp_Map = [[0]*N for _ in range(N)]
    temp_visit = [[0]*N for _ in range(N)]
    temp_vec = [[0]*N for _ in range(N)]
    temp_dir = [[[] for _ in range(N)] for _ in range(N)]
    
    move()
    Map = copy.deepcopy(temp_Map)
    visit = copy.deepcopy(temp_visit)
    dir = copy.deepcopy(temp_dir)
    vec = copy.deepcopy(temp_vec)

ans = 0
for y in range(N):
    for x in range(N):
        if visit[y][x] > 1:
            ans += Map[y][x]*4
        elif visit[y][x] == 1:
            ans += Map[y][x]
print(ans)